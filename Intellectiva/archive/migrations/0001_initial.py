# Generated by Django 4.2 on 2023-05-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paper",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=13)),
                ("description", models.TextField()),
                ("timestamp", models.DateTimeField(blank=True)),
                ("slug", models.SlugField(max_length=255, null=True)),
            ],
        ),
    ]