from dataclasses import field
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class NoteSerializer(ModelSerializer):
    class Meta:
        model= Note
        fields='__all__'

class FileSerializer(ModelSerializer):
    class Meta:
        model= File
        fields='__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields='__all__'

class GroupTaskSerializer(ModelSerializer):
    class Meta:
        model= GroupTask
        fields='__all__'


class TaskForGroupSerializer(ModelSerializer):
    class Meta:
        model= TaskForGroup
        fields='__all__'

