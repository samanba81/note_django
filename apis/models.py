from django.db import models


# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=15)
    userPass = models.CharField(max_length=20)

    def __str__(self):
        return f'User({self.userId} - {self.userName} - {len(self.userPass) * "*"})'


class Note(models.Model):
    noteId = models.AutoField(primary_key=True)
    noteTitle = models.CharField(max_length=50)
    noteContent = models.TextField()
    noteConnect = models.ForeignKey(User, on_delete=models.CASCADE)
    noteColor = models.CharField(max_length=10)

    def __str__(self):
        return f'Note({self.noteId} - {self.noteConnect} -> {self.noteColor} - {self.noteTitle} : {self.noteContent})'
