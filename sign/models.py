#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
# Create your models here.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'guest.settings'

# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100,verbose_name=u'发布会标题')
    limit = models.IntegerField(verbose_name=u'参加人数')
    status = models.BooleanField(verbose_name=u'状态')
    address = models.CharField(max_length=200,verbose_name=u'地址')
    start_time = models.DateTimeField(default=datetime.now,verbose_name=u'发布会时间')
    create_time = models.DateTimeField(auto_now=True,verbose_name=u'创建时间')

    class Meta:
        verbose_name=u'发布会'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event,verbose_name=u'关联发布会')
    realname = models.CharField(max_length=64,verbose_name=u'姓名')
    phone = models.CharField(max_length=16,verbose_name=u'手机号')
    email = models.EmailField(verbose_name=u'邮箱')
    sign = models.BooleanField(verbose_name=u'签到状态')
    create_time = models.DateTimeField(auto_now=True,verbose_name=u'创建时间')

    class Meta:
        verbose_name=u'嘉宾'
        verbose_name_plural=verbose_name
        unique_together = ("event", "phone")

    def __unicode__(self):
        return self.realname