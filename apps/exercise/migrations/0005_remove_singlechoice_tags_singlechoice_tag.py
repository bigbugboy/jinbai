# Generated by Django 4.2.8 on 2023-12-21 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_alter_singlechoice_choice_a_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlechoice',
            name='tags',
        ),
        migrations.AddField(
            model_name='singlechoice',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise.tag'),
        ),
    ]