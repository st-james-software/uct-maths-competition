# Generated by Django 4.2.7 on 2024-01-09 13:30

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0005_emailaddress_idx_upper_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
            ],
            options={
                'db_table': 'account_emailaddress',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.emailaddress',),
        ),
        migrations.CreateModel(
            name='EmailConfirmation',
            fields=[
            ],
            options={
                'db_table': 'account_emailconfirmation',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.emailconfirmation',),
        ),
    ]