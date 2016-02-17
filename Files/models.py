# -*- coding: utf-8 -*-

import os
import sys

from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
def path_and_rename(self, fn):
    ext = fn.split('.')[-1]
    # set filename as random string
    fn = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file

    return os.path.join("upload", fn)
    
# Create your models here.
class TOriFile(models.Model):
    link = models.IntegerField(default = 0, verbose_name = "关联数量")
    md5 = models.CharField(max_length = 40, verbose_name = "MD5")
    upload = models.FileField(null = True, upload_to = path_and_rename, verbose_name = "上传文件路径")
    path = models.TextField(verbose_name = "文件路径")
    name = models.TextField(verbose_name = "文件名")
    folder = models.TextField(null = True, verbose_name = "放置目录")
    create_time = models.DateTimeField(null = True, auto_now = True, verbose_name = "创建时间")
    mimetype = models.CharField(max_length = 40, null = True, verbose_name = "文件类型")

    def url(self):
        return "/static/{}".format(self.upload)
    
class TUserFolder(models.Model):
    master = models.IntegerField(null = True, verbose_name = "上级目录")
    user = models.ForeignKey(User)
    name = models.TextField(verbose_name = "目录名")
    create_time = models.DateTimeField(auto_now = True, verbose_name = "创建时间")

class TUserFile(models.Model):
    ori = models.ForeignKey(TOriFile, verbose_name = "原文件")
    user = models.ForeignKey(User, verbose_name = "所属用户")
    master = models.ForeignKey(TUserFolder, verbose_name = "所在目录")
    name = models.TextField(verbose_name = "文件名")
    create_time = models.DateTimeField(auto_now = True, verbose_name = "创建时间")

    def md5(self):
        return self.ori.md5

    def mimetype(self):
        return self.ori.mimetype

    def url(self):
        return self.ori.url()
    
