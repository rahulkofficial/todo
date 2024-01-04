from django.urls import path

from web import views

app_name="web"
urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('index',views.index,name='index'),
    path('add_task',views.add_task,name='add_task'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('revert/<int:id>',views.revert,name='revert'),
    path('complete/<int:id>',views.complete,name='complete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit/update/<int:id>',views.update,name='update'),
]

