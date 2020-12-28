# Generated by Django 3.1.4 on 2020-12-04 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=150)),
                ('branch_code', models.CharField(max_length=45, null=True)),
                ('manager', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=45, null=True)),
                ('loan_officer', models.CharField(max_length=200, null=True)),
                ('mobile', models.CharField(max_length=45, null=True)),
                ('address', models.CharField(max_length=355, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.district')),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.taluka')),
            ],
        ),
    ]