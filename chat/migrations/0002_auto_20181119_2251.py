# Generated by Django 2.1.3 on 2018-11-20 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Aluno'),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contas.Professor'),
        ),
    ]
