from django.db.models.signals import post_save
from django.dispatch import receiver

from quickbudget.models import Budget, Expense


@receiver(post_save, sender=Expense)
def interaction_with_budget(sender, instance, **kwargs):
    Budget.objects.get(id=instance.budget_id.id).save(
        update_fields=["last_interaction"]
    )
