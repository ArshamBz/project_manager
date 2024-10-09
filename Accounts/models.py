from django.db import models
from django.contrib.auth.models import User
from Projects.models import Project, Task, SubTask


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to='accounts/profile/',
                              default='accounts/profile/default/default_avatar.jpg')

    def __str__(self):
        return self.user.username

    @property
    def all_project(self):
        count = 0
        all_pj = Project.objects.filter(user=self.user)
        for pj in all_pj:
            count += 1
        return count

    @property
    def all_task(self):
        count = 0
        all_task = Task.objects.filter(project__user=self.user)
        for task in all_task:
            count += 1
        return count

    @property
    def all_sub_task(self):
        count = 0
        all_sub = SubTask.objects.filter(task__project__user=self.user)
        for sub in all_sub:
            count += 1
        return count

    @property
    def count_project(self):
        if self.all_project != 0:
            count = 0
            done = 0
            all_pj = Project.objects.filter(user=self.user)
            for pj in all_pj:
                count += 1
                if pj.status is True:
                    done += 1
            avg = (done / count)
            percentage = avg * 100
            return int(percentage)
        else:
            return 0

    @property
    def count_task(self):
        if self.all_task != 0:
            count = 0
            done = 0
            all_task = Task.objects.filter(project__user=self.user)
            for task in all_task:
                count += 1
                if task.status is True:
                    done += 1
            avg = (done / count)
            percentage = avg * 100
            return int(percentage)
        else:
            return 0

    @property
    def count_sub_task(self):
        if self.all_sub_task != 0:
            count = 0
            done = 0
            all_sub = SubTask.objects.filter(task__project__user=self.user)
            for sub in all_sub:
                count += 1
                if sub.status is True:
                    done += 1

            avg = (done / count)
            percentage = avg * 100
            return int(percentage)
        else:
            return 0