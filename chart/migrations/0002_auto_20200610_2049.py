# Generated by Django 2.1.1 on 2020-06-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GJrisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cor_code', models.IntegerField()),
                ('ODD', models.IntegerField()),
                ('PFS', models.IntegerField()),
                ('DMR', models.IntegerField()),
                ('ETC', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JNrisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cor_code', models.IntegerField()),
                ('ODD', models.IntegerField()),
                ('PFS', models.IntegerField()),
                ('DMR', models.IntegerField()),
                ('ETC', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='rankingdata',
            name='Cor_name',
            field=models.IntegerField(),
        ),
    ]
