from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication
from api.permissions import IsAdminOrReadOnly
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class NoteAPI(viewsets.ModelViewSet):
    # показываем что доступны все методы для работы с данными (post, get, put, delete запросы)
    queryset= Note.objects.all()
    # указываем сериализатор
    serializer_class = NoteSerializer 
    # устанавливаем классы для фильтрации 
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # указываем поле по которому проводить фильтрацию 
    search_fields = ['UserToken']

    def get_paginated_response(self, data):
       return Response(data)

class FileAPI(viewsets.ModelViewSet):
    # показываем что доступны все методы для работы с данными (post, get, put, delete запросы)
    queryset= File.objects.all()
    # указываем сериализатор
    serializer_class = FileSerializer 
    # устанавливаем классы для фильтрации 
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # указываем поле по которому проводить фильтрацию 
    search_fields = ['UserToken']

    def get_paginated_response(self, data):
       return Response(data)

class TaskAPI(viewsets.ModelViewSet):
    # показываем что доступны все методы для работы с данными (post, get, put, delete запросы)
    queryset= Task.objects.all()
    # указываем сериализатор
    serializer_class = TaskSerializer 
    # устанавливаем классы для фильтрации 
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # указываем поле по которому проводить фильтрацию 
    search_fields = ['UserToken']

    def get_paginated_response(self, data):
       return Response(data)

class GroupTaskAPI(viewsets.ModelViewSet):
    # показываем что доступны все методы для работы с данными (post, get, put, delete запросы)
    queryset= GroupTask.objects.all()
    # указываем сериализатор
    serializer_class = GroupTaskSerializer 
    # устанавливаем классы для фильтрации 
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # указываем поле по которому проводить фильтрацию 
    search_fields = ['UserToken']

    def get_paginated_response(self, data):
       return Response(data)

class TaskForGroupAPI(viewsets.ModelViewSet):
    # показываем что доступны все методы для работы с данными (post, get, put, delete запросы)
    queryset= TaskForGroup.objects.all()
    # указываем сериализатор
    serializer_class = TaskForGroupSerializer 
    # устанавливаем классы для фильтрации 
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # указываем поле по которому проводить фильтрацию 
    search_fields = ['Group_id',]

    def get_paginated_response(self, data):
       return Response(data)

