# Generated by Django 4.2.7 on 2023-11-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitRegisterRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_answer', models.CharField(choices=[('A', 'accepted'), ('D', 'decline'), ('P', 'pending')], default='P', max_length=1)),
                ('semester_course', models.ManyToManyField(related_name='unit_register_request', to='course.semestercourse')),
            ],
        ),
    ]
