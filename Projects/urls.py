from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectDeleteView, UpdateProjectView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('create/project', ProjectCreateView.as_view(), name='project_create'),
    path('delete/project/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('update/project/<int:pk>/', UpdateProjectView.as_view(), name='project_update'),
]
