from rest_framework import serializers
from Files.models import *

class OriFileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TOriFile
        fields = ("id", "upload", "md5", "name", "mimetype", "url", "folder")
        read_only_fields = ("id", "md5", "name", "mimetype", "url")
        

class UserFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUserFolder
        fields = ('id', 'create_time', 'name', 'master', 'user')
        read_only_fields = ('id', 'create_time', 'user')

class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUserFile
        fields = ('id', 'md5', 'create_time', 'mimetype', 'name', 'url', 'master', 'user')
        read_only_fields = ('id', 'md5', 'create_time', 'mimetype', 'url', 'user')
