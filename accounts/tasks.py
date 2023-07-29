from celery import shared_task
from datetime import datetime, timedelta
from accounts.models import OtpCode
from pytz import timezone

def remove_expired_otp_codes():
    expired_time = datetime.now(tz=timezone('Asia/Tehran')) - timedelta(minutes=2)
    OtpCode.filter(created__lt=expired_time).delete()
