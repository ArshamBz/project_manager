from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm, ProjectUpdateForm


class ProjectListView(LoginRequiredMixin, ListView):
    """
    this view will return all of the projects
    """
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        context = {
            'projects': projects
        }
        return render(request, 'Projects/projects.html', context)


class ProjectCreateView(CreateView):
    """
    this view give us create function for project model
    """

    form_class = ProjectForm
    template_name = 'Projects/create_project.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, request.FILES,)
        if form.is_valid():
            data = form.cleaned_data
            project = Project.objects.create(
                user=user,
                title=data['title'], image=data['image'],
                description=data['description'], color=data['color'],
                start_date=data['start_date'], end_date=data['end_date'],
                budget=data['budget']
            )
            if project:
                messages.success(request, 'your project saved', 'success')
                return redirect('projects:projects_list')
            messages.error(request, 'something went wrong !!!', 'danger')
        else:
            form = self.form_class()
        return render(request, 'Projects/create_project.html', {"form": form})


class ProjectDeleteView(DeleteView):
    """
        ...
    """
    model = Project
    pk_url_kwarg = 'pk'
    template_name = 'Projects/confirm_delete_pj.html'
    success_url = '/'


class UpdateProjectView(UpdateView):
    """
    ...
    """
    model = Project
    form_class = ProjectUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'Projects/update.html'
    success_url = '/'