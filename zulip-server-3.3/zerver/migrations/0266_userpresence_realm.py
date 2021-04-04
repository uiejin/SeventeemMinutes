# Generated by Django 1.11.28 on 2020-02-08 20:19
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0265_remove_stream_is_announcement_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpresence',
            name='realm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zerver.Realm'),
        ),
    ]
