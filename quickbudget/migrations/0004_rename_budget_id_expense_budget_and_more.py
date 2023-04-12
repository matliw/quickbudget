# Generated by Django 4.1.7 on 2023-04-11 09:01

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickbudget', '0003_alter_budget_budget_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='budget_id',
            new_name='budget',
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget_limit',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='expense',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
