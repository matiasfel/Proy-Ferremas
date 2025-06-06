# Generated by Django 5.2 on 2025-05-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_producto_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precio',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='precio',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterUniqueTogether(
            name='precio',
            unique_together={('producto', 'fecha')},
        ),
    ]
