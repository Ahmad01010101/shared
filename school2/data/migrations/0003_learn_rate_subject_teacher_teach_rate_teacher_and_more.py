# Generated by Django 4.0.4 on 2022-05-22 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0002_rename_bearth_date_student_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fainal_mark', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.student')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.BooleanField()),
                ('attention', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('behavior', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('interaction', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('communiction_skills', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('leadership_skills', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('team_skills', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('logical_thinking', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('critical_thinking', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('creative_thinking', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('proplem_solving', models.IntegerField(blank=True, choices=[(1, 'Bad'), (2, 'Medieum'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('nots', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('class_num', models.IntegerField()),
                ('learning', models.ManyToManyField(through='data.Learn', to='data.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('mid_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('certification', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('is_manager', models.BooleanField()),
                ('rate_students', models.ManyToManyField(through='data.Rate', to='data.student')),
                ('teacher_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.teacher'),
        ),
        migrations.AddField(
            model_name='learn',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.subject'),
        ),
        migrations.CreateModel(
            name='Documintation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body_text', models.CharField(max_length=255)),
                ('file_body', models.FileField(upload_to='files')),
                ('date', models.DateField()),
                ('teacher_publish_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Declirations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50000)),
                ('body_text', models.TextField()),
                ('body_img', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('teacher_publish_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.teacher')),
            ],
        ),
    ]