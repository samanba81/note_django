from django.http import HttpResponse
from django.template import loader
from apis.models import User, Note


# Create your views here.


def login(request):
    template = loader.get_template('account/login.html')
    if request.method == 'GET':
        return HttpResponse(template.render({}, request))
    else:
        userName = request.POST['userName']
        userPass = request.POST['userPass']
        userSelect = User.objects.filter(userName=userName)
        if userSelect.exists():
            if userSelect.first().userPass == userPass:
                template = loader.get_template('notes.html')
                noteList = Note.objects.filter(noteConnect=userSelect.first())
                return HttpResponse(template.render({
                    'message': 'isOk',
                    'notes': noteList
                }, request))
            else:
                return HttpResponse(template.render({'message': 'passNotTrue'}, request))
        else:
            return HttpResponse(template.render({'message': 'userNotFond'}, request))


def register(request):
    if request.method == 'GET':
        template = loader.get_template('account/register.html')
        return HttpResponse(template.render({}, request))
    else:
        pass


def notes(request):
    pass
