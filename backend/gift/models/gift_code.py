from django.db import models


class GiftCode(models.Model):
    class Meta:
        verbose_name = "Gift Code"
        verbose_name_plural = "Gift Codes"

    is_general = models.BooleanField(default=False)
    
    gift_code_type = models.IntegerField()

    
    GIFT_CODE_TYPES=(
        (0, "PERCENT_BASE"),
        (1, "PRICE_BASE"),
    )
    gift_code_type = models.IntegerField(choices=GIFT_CODE_TYPES)