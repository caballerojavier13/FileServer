# -*- coding: utf-8 -*-
# Create your views here.
import hashlib
from datetime import datetime
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Files.serializers import *
from Files.models import *

class OriFileViewSet(viewsets.ModelViewSet):
    '''上传文件视图
    '''
    queryset = TOriFile.objects.all()
    serializer_class = OriFileSerilizer

    def perform_create(self, serializer):
        md5 = hashlib.md5()
        upfile = self.request.FILES['upload']
        
        for chunk in upfile.chunks():
            md5.update(chunk)
        hex_md5 = md5.hexdigest()

        kwargs = {'md5': hex_md5,
                  'link': 1,
                  'create_time': datetime.now(),
                  'mimetype': upfile.content_type,
                  'name': upfile.name}

        # objs = self.queryset.filter(md5 = hex_md5)
        # if 0 < len(objs):
        #     # 已经存在md5码相同的文件，映射到同一个文件即可
        #     kwargs['path'] = objs[0].path
        
        instance = serializer.save(**kwargs)
        folder = instance.folder
        
        def make_path(user, master, folder):
            if "" == folder or None == folder:
                return master

            lst = folder.split("/")
            try:
                uf = TUserFolder.objects.get(user = user, master = master, name = lst[0])
            except:
                uf = TUserFolder(user = user, master = master, name = lst[0])
                uf.save()

            return make_path(user, uf.id, "/".join(lst[1:]))

        master = make_path(self.request.user, 0, folder)
        print("Master: {}".format(master))

        userfile = TUserFile(ori = instance,
                             user = self.request.user,
                             master_id = master,
                             name = instance.name)
        userfile.save()
        
class UserFilesViewSet(viewsets.ModelViewSet):
    """文件视图
    """
    queryset = TUserFile.objects.all()
    serializer_class = UserFileSerializer

class UserFoldersViewSet(viewsets.ModelViewSet):
    '''目录视图
    '''
    queryset = TUserFolder.objects.all()
    serializer_class = UserFolderSerializer
    
    def perform_create(self, serializer):
        kwargs = {'user': self.request.user,
                  'create_time': datetime.now()}
        serializer.save(**kwargs)
