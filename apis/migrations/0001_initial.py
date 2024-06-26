# Generated by Django 5.0.6 on 2024-05-24 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("userId", models.AutoField(primary_key=True, serialize=False)),
                ("userName", models.CharField(max_length=15)),
                ("userPass", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                ("noteId", models.AutoField(primary_key=True, serialize=False)),
                ("noteTitle", models.CharField(max_length=50)),
                ("noteContent", models.TextField()),
                (
                    "noteConnect",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="apis.user"
                    ),
                ),
            ],
        ),
    ]
