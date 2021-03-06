# Generated by Django 3.0.6 on 2020-08-21 12:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_Id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Id', models.CharField(max_length=200)),
                ('Date_Time', models.DateTimeField(auto_now_add=True)),
                ('Status', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('Total_Amount', models.IntegerField()),
                ('Refund_Amount', models.IntegerField()),
                ('User_Id', models.ForeignKey(on_delete=models.SET('Deleted'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
