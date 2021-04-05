from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('issue<int:issue_num>/', views.issue, name='issuetoc'),
    path('issue<int:issue_num>/<slug:slug>', views.content_detail, name='contentdetail'),
    path('contributors/', views.contributors, name='contributors'),
    path('current/', views.current, name='current'),
]