from . import views
from django.urls import path, include, re_path 
from rest_framework import routers

routNote= routers.SimpleRouter()
routNote.register(r'NoteAPI', views.NoteAPI)

routFile= routers.SimpleRouter()
routFile.register(r'FileAPI', views.FileAPI)

routTask= routers.SimpleRouter()
routTask.register(r'TaskAPI', views.TaskAPI)

routGroupTask= routers.SimpleRouter()
routGroupTask.register(r'GroupTaskAPI', views.GroupTaskAPI)

routTaskForGroup = routers.SimpleRouter()
routTaskForGroup.register(r'TaskForGroupAPI', views.TaskForGroupAPI)

urlpatterns = [
    path("NoteAPI/", include(routNote.urls)),
    path("FileAPI/", include(routFile.urls)),
    path("TaskAPI/", include(routTask.urls)),
    path("GroupTaskAPI/", include(routGroupTask.urls)),
    path("TaskForGroupAPI/", include(routTaskForGroup.urls)),
]