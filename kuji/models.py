from django.db import models


class Member(models.Model):
    no = models.CharField('社員番号', max_length=6, unique=True)
    is_attendance = models.BooleanField('出席？')
    seat = models.IntegerField('座席番号', null=True, blank=True)


class Seat(models.Model):
    rest_no = models.IntegerField('空いている座席番号')
