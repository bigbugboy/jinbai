# Generated by Django 4.2.8 on 2023-12-21 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0006_alter_singlechoice_no_alter_singlechoice_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlechoice',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise.tag'),
        ),
    ]
