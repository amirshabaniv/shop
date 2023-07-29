from typing import Any, Optional
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from accounts.models import OtpCode
from pytz import timezone



class Command(BaseCommand):
    help = 'Remove all expired otp\'s codes'

    def handle(self, *args, **options):
        expired_time = datetime.now(tz=timezone('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write('All expired otp\'s codes removed')