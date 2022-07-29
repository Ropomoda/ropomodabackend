from django.db import models
from app.models import Extensions


class Notice(Extensions):
    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"
        
    to = models.ForeignKey('account.User' , on_delete=models.CASCADE)
    should_send_sms = models.BooleanField(default=False)
    should_send_email = models.BooleanField(default=False)
    should_send_alert = models.BooleanField(default=False)

    title = models.CharField(max_length=250 , null=True , blank=True , default='')
    body = models.TextField(null=True , blank=True , default='')
    type_code = models.IntegerField(default=0 , null=True , blank=True)
    def __str__(self) -> str:
        return f'{self.to.mobile} {self.title}'