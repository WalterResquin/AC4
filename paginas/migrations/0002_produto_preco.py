# Generated by Django 2.2.4 on 2019-09-11 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=5, max_digits=5, null=True),
        ),
    ]
