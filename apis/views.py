from .serializers import NoteSerializer, NoteAdminSerializer, UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Notes.settings import DEBUG, ADMIN_INFO
from django.http import JsonResponse
from apis.models import User, Note


# Create your views here.


@api_view(['POST'])
def create_user(request):
    """for create user"""
    if request.method == 'POST':
        data = request.POST
        username = data['userName']
        password = data['userPass']
        haveUser = User.objects.get(userName=username)
        if haveUser:
            return JsonResponse({'message': 'WeHaveThisUserName'}, status=409)
        user = User(userName=username, userPass=password)
        user.save()
        if DEBUG:
            print(f'userCreated -> {username} - {password}')
        return JsonResponse({'message': 'UserCreated'}, status=200)
    else:
        return JsonResponse({'message': 'MethodNotAllowed'}, status=405)


@api_view(['POST'])
def create_note(request):
    """for create note"""
    if request.method == 'POST':
        data = request.POST
        userName = data['userName']
        userPass = data['userPass']
        try:
            user = User.objects.get(userName=userName)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'UserNotExist'}, status=404)
        if user.userPass == userPass:
            title = data['title']
            content = data['content']
            color = data['color']
            note = Note(noteTitle=title, noteContent=content, noteConnect=user,noteColor=color)
            note.save()
            notesObject = Note.objects.filter(noteConnect=user.userId)
            serializer = NoteSerializer(notesObject, many=True)
            if DEBUG:
                print(f'noteCreated -> {userName} - {title}')
            return JsonResponse({
                'message': 'NoteCreated',
                'notes': serializer.data
            }, status=200)
        else:
            return JsonResponse({'message': 'WrongPassword'}, status=400)
    else:
        return JsonResponse({'message': 'MethodNotAllowed'}, status=405)


@api_view(['GET'])
def get_notes(request):
    """for get notes"""
    if request.method == 'GET':
        data = request.GET
        userName = data['userName']
        userPass = data['userPass']

        if userName == ADMIN_INFO['userName'] and userPass == ADMIN_INFO['userPass']:
            usersObject = User.objects.all()
            notesObject = Note.objects.all()

            serializerNote = NoteAdminSerializer(notesObject, many=True)
            serializerUser = UserSerializer(usersObject, many=True)

            return JsonResponse({
                'message': "WelcomeAdmin",
                'users': serializerUser.data,
                'notes': serializerNote.data,
            })
        try:
            user = User.objects.get(userName=userName)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'UserNotExist'}, status=404)

        if user.userPass == userPass:
            notes = Note.objects.filter(noteConnect=user)
            serializer = NoteSerializer(notes, many=True)
            return Response({
                'message': 'Ok',
                'notes': serializer.data
            })
        else:
            return JsonResponse({'message': 'InvalidPassword'}, status=401)
    else:
        return JsonResponse({'message': 'MethodNotAllowed'}, status=405)


@api_view(['POST'])
def edit_note(request):
    """for edit notes"""
    if request.method == 'POST':
        data = request.data
        userName = data['userName']
        userPass = data['userPass']
        try:
            user = User.objects.get(userName=userName)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'UserNotFound'}, status=404)
        if user.userPass == userPass:
            noteId = data['noteId']
            try:
                note = Note.objects.get(noteConnect=user, noteId=noteId)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'NoteNotFound'}, status=404)
            title = data['title']
            content = data['content']
            color = data['color']
            note.noteTitle = title
            note.noteContent = content
            note.noteColor = color
            note.save()
            notes = Note.objects.filter(noteConnect=user)
            serializer = NoteSerializer(notes, many=True)
            return Response({'message': 'EditOk', 'notes': serializer.data}, status=200)
        else:
            return JsonResponse({'message': 'WrongPassword'}, status=405)
    else:
        return JsonResponse({'message': 'MethodNotAllowed'}, status=405)


@api_view(['POST'])
def delete_note(request):
    data = request.POST
    userName = data['userName']
    userPass = data['userPass']
    try:
        user = User.objects.get(userName=userName)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'user not found'}, status=404)
    if user.userPass == userPass:
        noteId = data['noteId']
        try:
            note = Note.objects.get(noteConnect=user, noteId=noteId)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'note not found'}, status=404)
        note.delete()
        notes = Note.objects.filter(noteConnect=user)
        serializer = NoteSerializer(notes, many=True)
        return Response({'message': 'DeleteOk', 'notes': serializer.data}, status=200)
    else:
        return JsonResponse({'message': 'wrong password'}, status=400)
