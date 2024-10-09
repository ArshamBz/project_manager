from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task, SubTask
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm, ProjectUpdateForm, TaskForm, UpdateTaskForm, SubTaskForm, UpdateSubTaskForm
from django.contrib.auth.models import User


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
        form = self.form_class(request.POST, request.FILES, )
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


class TaskListView(ListView):
    """
        this views give us detail of project and all task of this project
        """

    def get(self, request, *args, **kwargs):
        projects = get_object_or_404(Project, id=kwargs['id'])
        tasks = Task.objects.filter(project=projects)

        context = {
            'projects': projects,
            'tasks': tasks,
        }
        return render(request, 'Projects/task.html', context)


class DeleteTask(DeleteView):
    """
        this views give us delete func of task
        """
    model = Task
    pk_url_kwarg = 'pk'
    template_name = 'Projects/confirm_delete_ts.html'
    success_url = '/'


class UpdateTask(UpdateView):
    """
        this views give us update task func
        """
    model = Task
    form_class = UpdateTaskForm
    pk_url_kwarg = 'pk'
    template_name = 'Projects/update_ts.html'
    success_url = '/'


class AllTaskListView(ListView):
    """
        this views give us all task of this user
        """

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(project__user=request.user)
        context = {
            'tasks': tasks,
        }
        return render(request, 'Projects/all_tasks.html', context)


class TaskCreateView(CreateView):
    """
    this views give us create function for task model
    """
    form_class = TaskForm
    template_name = 'Projects/create_task.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user)
        project = Project.objects.get(id=self.kwargs['id'])
        if form.is_valid():
            data = form.cleaned_data
            task = Task.objects.create(
                project=project, image=data['image'],
                color=data['color'], descriptions=data['descriptions'],
                start_date=data['start_date'], end_date=data['end_date'], title=data['title']
            )
            if task:
                messages.success(request, 'your task saved success', 'success')
                return redirect('project:all_task', project.id)
            else:
                messages.error(request, 'somthing went wrong !!', 'danger')
                return redirect('project:all_task', project.id)

        else:
            form = self.form_class(instance=user)
        return render(request, 'Projects/create_task.html', {"form": form})


class TaskAndSubTaskListView(ListView):
    """
        this views give us detail of task and subtask
        """

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        task = get_object_or_404(Task, id=kwargs['id'])
        sub_task = SubTask.objects.filter(task=task)

        context = {
            'task': task,
            'sub_task': sub_task,
        }
        return render(request, 'Projects/task_detail.html', context)


class SubTaskCreateView(CreateView):
    """
    this views give us create function for subtask model
    """
    form_class = SubTaskForm
    template_name = 'Projects/create_subtask.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user)
        task = Task.objects.get(id=self.kwargs['id'])
        if form.is_valid():
            data = form.cleaned_data
            sub_task = SubTask.objects.create(
                task=task, image=data['image'],
                color=data['color'], descriptions=data['descriptions'],
                start_date=data['start_date'], end_date=data['end_date'], title=data['title']
            )
            if sub_task:
                messages.success(request, 'your sub task saved success', 'success')
                return redirect('project:task_detail', task.id)
            else:
                messages.error(request, 'somthing went wrong !!', 'danger')
                return redirect('project:task_detail', task.id)

        else:
            form = self.form_class(instance=user)
        return render(request, 'Projects/create_subtask.html', {"form": form})


class DeleteSubTask(DeleteView):
    """
        this views give us delete func of subtask model
        """
    model = SubTask
    pk_url_kwarg = 'pk'
    template_name = 'Projects/confirm_delete_st.html'
    success_url = '/'


class UpdateSubTask(UpdateView):
    """
        this views give us update func for subtask model
        """
    model = SubTask
    form_class = UpdateSubTaskForm
    pk_url_kwarg = 'pk'
    template_name = 'Projects/update_st.html'
    success_url = '/'


class SubTaskView(ListView):
    """
            this views give us detail of subtask
            """

    def get(self, request, *args, **kwargs):
        sub_task = get_object_or_404(SubTask, id=kwargs['id'])

        context = {
            'sub_task': sub_task,
        }
        return render(request, 'Projects/subtask.html', context)
