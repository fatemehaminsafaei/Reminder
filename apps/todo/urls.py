from django.urls import path, include
from . import views
from apps.todo.views import TaskList, TaskDetail, CategoryList, IndexPage, Lists, TaskListAPI
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexPage.as_view(), name='Home'),
    path('', TaskList.as_view(), name='task_list'),
    path('post/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('newtask/', views.task_new, name='add_new_task'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('newcategory/', views.category_new, name='add_new_category'),
    path('categories/', include([
        path('', CategoryList.as_view(), name='categories'),
        path('<slug:slug>/', Lists.as_view(), name='Lists'),
    ])),
    path('common/', include([
        path('ok/', TemplateView.as_view(template_name='successfully.html'), name='ok'),
        path('404/', TemplateView.as_view(template_name='404.html'), name='404')
    ]
    ), ),
    path('task_list_json/', TaskListAPI.as_view(), name='task_list_json')
]
