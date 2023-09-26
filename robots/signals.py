from orders.utils import send_email_for_robots_waitlist
from robots.models import Robot
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Robot)
def robot_created_handler(sender, instance, created, **kwargs):
    if created:
        send_email_for_robots_waitlist(instance.serial, instance.model, instance.version)