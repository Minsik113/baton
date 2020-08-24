from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'accounts'

class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name="상품이름")
    description = models.TextField(verbose_name="상품설명")
    want = models.CharField(max_length=32, verbose_name="원하는물건")
    postalcode = models.IntegerField(verbose_name="우편번호",null=True)
    juso1 = models.TextField(verbose_name="주소지",null=True)
    juso2 = models.TextField(verbose_name="상세주소",null=True)
    tradedetail = models.TextField(verbose_name="교환방법",null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "baton_Product"
        verbose_name = "상품"
        verbose_name_plural = "상품"