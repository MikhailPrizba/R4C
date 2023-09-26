from orders.models import Order
from django.core import mail


def send_email_for_robots_waitlist(robot_serial: str, robot_model: str, robot_version: str):
    orders = Order.objects.select_related("customer").filter(robot_serial=robot_serial)

    for order in orders:
        email = order.customer.email
        message = f"Добрый день! \n\nНедавно вы интересовались нашим роботом модели {robot_model}, версии {robot_version}. \n\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"
        mail.send_mail(
            "Робот в наличии",
            message,
            "noreply@company.com",
            [email],
        )