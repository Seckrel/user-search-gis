from celery.schedules import crontab
from celery import Celery
from celery.utils.log import get_task_logger
from .models import UserProfile
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail
import os


app = Celery("user_search_gis")

app.conf.enable_utc = False

app.conf.update(timezone="Asia/Kathmandu")

logger = get_task_logger(__name__)


@shared_task(bind=True)
def wish_by_email(self):
    print("working here")
    users_w_bday = UserProfile.objects.filter(
        birthday=timezone.now().date().isoformat())
    for user in users_w_bday:
        send_mail(
            "Wishing You Many Many Return of the Day",
            f"From entire Naxa team we wish you a amazing birthday {user.first_name}, ",
            os.environ.get("EMAIL_USER", ""),
            [user.user.email],
            fail_silently=False,
        )
