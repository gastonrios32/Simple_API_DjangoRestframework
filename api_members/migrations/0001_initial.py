# Generated by Django 4.1.1 on 2022-09-22 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TlbJobPosition',
            fields=[
                ('id_position', models.AutoField(primary_key=True, serialize=False)),
                ('desc_position', models.CharField(db_column='Desc_position', max_length=100)),
            ],
            options={
                'db_table': 'tlb_job_Position',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TlbMembers',
            fields=[
                ('id_member', models.IntegerField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=100)),
                ('status_memb', models.IntegerField(default=1)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tlb_members',
                'ordering': ['id_member'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TlbStatusCivil',
            fields=[
                ('id_civilstatus', models.AutoField(primary_key=True, serialize=False)),
                ('desc_civil', models.CharField(db_column='Desc_civil', max_length=100)),
            ],
            options={
                'db_table': 'tlb_status_Civil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TlbMemberJob',
            fields=[
                ('job_id', models.AutoField(db_column='Job_ID', primary_key=True, serialize=False)),
                ('date_entry', models.DateField(verbose_name='Fecha de Ingreso')),
                ('direction', models.CharField(blank=True, max_length=250, null=True)),
                ('job_name', models.CharField(blank=True, db_column='Job_name', max_length=150, null=True)),
                ('id_member', models.ForeignKey(db_column='id_member', on_delete=django.db.models.deletion.CASCADE, to='api_members.tlbmembers')),
                ('id_position', models.ForeignKey(db_column='id_position', on_delete=django.db.models.deletion.CASCADE, to='api_members.tlbjobposition')),
            ],
            options={
                'db_table': 'tlb_member_job',
                'ordering': ['id_member'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TlbMemberEmail',
            fields=[
                ('id_email', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('id_member', models.ForeignKey(db_column='id_member', on_delete=django.db.models.deletion.CASCADE, to='api_members.tlbmembers')),
            ],
            options={
                'db_table': 'tlb_member_email',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TlbMemberDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_bith', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direction', models.CharField(blank=True, max_length=250, null=True)),
                ('dependents', models.IntegerField(blank=True, db_column='Dependents', null=True)),
                ('civil_status', models.ForeignKey(db_column='Civil_status', on_delete=django.db.models.deletion.CASCADE, to='api_members.tlbstatuscivil')),
                ('id_member', models.ForeignKey(db_column='id_member', on_delete=django.db.models.deletion.CASCADE, to='api_members.tlbmembers')),
            ],
            options={
                'db_table': 'tlb_member_detail',
                'ordering': ['id_member'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='tlb_member_phone',
            fields=[
                ('id_contact', models.AutoField(primary_key=True, serialize=False)),
                ('phone1', models.CharField(blank=True, db_column='Phone1', max_length=50, null=True)),
                ('type_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('status_fone', models.IntegerField(blank=True, default=1, null=True)),
                ('id_member', models.ForeignKey(db_column='id_member', on_delete=django.db.models.deletion.CASCADE, to='api_members.tlbmembers')),
            ],
            options={
                'db_table': 'tlb_member_phone',
                'managed': True,
            },
        ),
    ]