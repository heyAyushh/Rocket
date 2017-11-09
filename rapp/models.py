# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4

# Create your models here.


class SignUpModel(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=120, unique=True, null=False, blank=False)
    password = models.TextField(max_length=40, null=False, blank=False)


class SessionModel(models.Model):
    user = models.ForeignKey(SignUpModel)
    session_token = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid4()


class DeviceModel(models.Model):
    user = models.ForeignKey(SignUpModel)
    deviceName = models.CharField(max_length=120)
    device_on = False

    @property
    def like_count(self):
        return len(ToggleModel.objects.filter(device=self))


class ToggleModel(models.Model):
    user = models.ForeignKey(SignUpModel)
    device = models.ForeignKey(DeviceModel)

# class RoomModel(models.Model):
#     room = models.CharField(max_length=255)
#
#
# class ToggleModel(models.Model):
#     room = models.ForeignKey(RoomModel)
#     device = models.CharField(max_length=255)
#     device_on = False
