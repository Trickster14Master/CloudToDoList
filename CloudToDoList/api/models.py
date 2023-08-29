from django.db import models

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Note(models.Model):
    NameNote = models.TextField(null=True)
    DescriptionNote = models.TextField(null=True)
    UserToken = models.TextField(default="")

    class Meta:
        ordering = ['NameNote']

    def __str__(self):
        return self.NameNote[0:50]


class File(models.Model):
    NameFile = models.TextField(null=True)
    File = models.FileField(upload_to=upload_to)
    UserToken = models.TextField(default="")

    class Meta:
        ordering = ['NameFile']

    def __str__(self):
        return self.NameFile[0:50]


class Task(models.Model):
    UserToken = models.TextField(default="")
    NameTask = models.TextField(null=True)
    DescriptionTask = models.TextField(null=True)
    DateTask = models.DateField(auto_now_add=True)
    StatusTask= models.BooleanField(default=False)
    FileForTask = models.FileField(upload_to=upload_to)

    class Meta:
        ordering = ['NameTask']

    def __str__(self):
        return self.NameTask[0:50]
    

class GroupTask(models.Model):
    UserToken = models.TextField(default="")
    NameGroupTask = models.TextField(null=True)
    StatusGroupTask= models.BooleanField(default=False)

    class Meta:
        ordering = ['NameGroupTask']

    def __str__(self):
        return self.NameGroupTask[0:50]


class TaskForGroup(models.Model):
    UserToken = models.TextField(default="")
    NameTaskForGroup= models.TextField(null=True)
    DescriptionTask = models.TextField(null=True)
    StatusTaskForGroup= models.BooleanField(default=False)
    Group = models.ForeignKey(GroupTask, on_delete = models.CASCADE)
    
    class Meta:
        ordering = ['NameTaskForGroup']

    def __str__(self):
        return self.NameTaskForGroup[0:50]
    
    @property
    def Group_id(self):
        return self.Group.id