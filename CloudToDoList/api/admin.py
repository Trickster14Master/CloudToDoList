from django.contrib import admin

from .models import Note
admin.site.register(Note)

from .models import File
admin.site.register(File)

from .models import Task
admin.site.register(Task)

from .models import GroupTask
admin.site.register(GroupTask)

from .models import TaskForGroup
admin.site.register(TaskForGroup)
