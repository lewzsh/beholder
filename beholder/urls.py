from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('backissues/', views.archive, name='archive'),
    path('issuedetails/<int:id>', views.issue, name='issuetoc'),
    path('contentdetails/<int:id>', views.content_detail, name='contentdetail'),
    path('contributors/', views.contributors, name='contributors')
]