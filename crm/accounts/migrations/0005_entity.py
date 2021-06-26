# Generated by Django 3.2.4 on 2021-06-24 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_parententityname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('is_disabled', models.BooleanField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('is_barcode', models.BooleanField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('sub_url', models.CharField(max_length=200, null=True)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.parententityname')),
            ],
        ),
    ]
