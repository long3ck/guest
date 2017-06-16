#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
# Create your models here.


# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100,verbose_name='发布会标题') # 发布会标题
    limit = models.IntegerField(verbose_name='参加人数') # 参加人数
    status = models.BooleanField(verbose_name='状态') # 状态
    address = models.CharField(max_length=200,verbose_name='地址') # 地址
    start_time = models.DateTimeField(default=datetime.now,verbose_name='发布会时间') # 发布会时间
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间') # 创建时间（自动获取当前时间）

    class Meta:
        verbose_name='发布会'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event,verbose_name='关联发布会') # 关联发布会 id
    realname = models.CharField(max_length=64,verbose_name='姓名') # 姓名
    phone = models.CharField(max_length=16,verbose_name='手机号') # 手机号
    email = models.EmailField(verbose_name='邮箱') # 邮箱
    sign = models.BooleanField(verbose_name='签到状态') # 签到状态
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间') # 创建时间（自动获取当前时间）

    class Meta:
        verbose_name='嘉宾'
        verbose_name_plural=verbose_name
        unique_together = ("event", "phone")

    def __unicode__(self):
        return self.realname