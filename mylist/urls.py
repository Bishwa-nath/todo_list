from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='todo-home'),
    path('addtask/', views.addtasks, name='tasks'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatetask/<int:id>', views.updatetask, name='updatetask'),
]
