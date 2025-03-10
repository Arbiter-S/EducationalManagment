# Generated by Django 4.2.7 on 2023-11-08 17:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('department', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('national_code', models.CharField(blank=True, max_length=10, null=True, validators=[user.validators.national_code])),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[user.validators.phone_number])),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, validators=[user.validators.birth_date])),
                ('role', models.CharField(blank=True, choices=[('STU', 'Student'), ('PRO', 'Professor'), ('AST', 'Assistant'), ('ADM', 'Admin')], max_length=3, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ITAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'IT Admin',
                'verbose_name_plural': 'IT Admins',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('expertise', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('P', 'Professor'), ('S', 'Supervisor'), ('L', 'Lecturer')], default='P', max_length=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.department')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.major')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professors',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('degree', models.CharField(choices=[('B', 'Bachelor'), ('M', 'Master'), ('D', 'Doctoral')], default='B', max_length=1)),
                ('entry_year', models.CharField(max_length=4)),
                ('entry_semester', models.CharField(max_length=255)),
                ('average', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('is_soldier', models.BooleanField(default=False)),
                ('military_status', models.CharField(blank=True, max_length=255, null=True)),
                ('academic_terms', models.PositiveIntegerField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.department')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.major')),
                ('passed_courses', models.ManyToManyField(related_name='student_passed_course', to='course.approvedcourse')),
                ('passing_courses', models.ManyToManyField(related_name='student_passing_course', to='course.semestercourse')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.professor')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='EducationalAssistant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.department')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.major')),
            ],
            options={
                'verbose_name': 'Educational Assistant',
                'verbose_name_plural': 'Educational Assistants',
            },
        ),
    ]
