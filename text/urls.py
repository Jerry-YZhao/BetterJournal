from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # URL pattern for the task completion view
    path('task-completion/', views.task_completion_view, name='task_completion'),

    # Include the admin URLs
    path('admin/', admin.site.urls),
]