# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Produto(models.Model):

    #__Produto_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    valor = models.CharField(max_length=255, null=True, blank=True)

    #__Produto_FIELDS__END

    class Meta:
        verbose_name        = _("Produto")
        verbose_name_plural = _("Produto")


class Clinte(models.Model):

    #__Clinte_FIELDS__
    nome_cliente = models.TextField(max_length=255, null=True, blank=True)
    documento = models.IntegerField(null=True, blank=True)

    #__Clinte_FIELDS__END

    class Meta:
        verbose_name        = _("Clinte")
        verbose_name_plural = _("Clinte")


class Venda(models.Model):

    #__Venda_FIELDS__
    produto = models.IntegerField(null=True, blank=True)
    clinte = models.IntegerField(null=True, blank=True)

    #__Venda_FIELDS__END

    class Meta:
        verbose_name        = _("Venda")
        verbose_name_plural = _("Venda")



#__MODELS__END
