# Generated by Django 4.0.1 on 2022-01-18 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_alter_comment_options_rename_author_cart_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
    ]