from django.shortcuts import render
from django.views.generic import ListView
from .models import Project


class ProjectListView(ListView):
    """
    this view will return all of the projects
    """

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        context = {
            'projects': projects
        }
        return render(request, 'Projects/projects.html', context)
