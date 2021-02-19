# Generated by Django 3.1.6 on 2021-02-18 15:56

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='TMT', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(1)], verbose_name='Amount'),
        ),
    ]
