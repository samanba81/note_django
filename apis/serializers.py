from rest_framework.serializers import ModelSerializer
from .models import User, Note


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'userName']


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['noteId', 'noteTitle', 'noteContent', 'noteColor']


class NoteAdminSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
