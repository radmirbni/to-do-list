from django.urls import path, include
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, TaskReorder
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
import debug_toolbar
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path("logout/", LogoutView.as_view(), name="logout"),
    path('/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('', cache_page(60*15)(TaskList.as_view()), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path("__debug__/", include("debug_toolbar.urls")),
]
