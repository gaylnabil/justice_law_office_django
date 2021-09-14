
from django.views.static import serve
from django.urls import path
from clients import views

urlpatterns = [
    path('clients', views.justice_clients, name='justice_clients'),
    # path('attorneys/', views.attorneys_list, name='attorneys_list'),
    # path('attorneys/<str:id>/', views.attorney_details, name='attorney_details'),
    # path('contact/', views.contact, name='contact'),
    # path('faq/', views.faq, name='faq'),
    # path('questions/', views.justice_question, name='justice_question'),
    # path('questions/<int:id>/comments',
    #      views.justice_comments, name='justice_comments'),

    # path('content_subcomment/<int:id>',
    #      views.content_subcomment, name='content_subcomment'),

    # path('justice/<int:id>/<str:name>',
    #      views.justice_delete, name='justice_delete'),

    # path('comments/<int:id>/subcomments',
    #      views.justice_subcomments, name='justice_subcomments')


    # path('project/staff/thanks/', views.thanks, name='thanks'),
    # path('project/task_team/', views.task_team, name='task_team'),
    # path('projects_list/', views.projects_list, name='projects_list'),
    # path('project/send/<str:encrypt_project_id>/', views.send_project, name='send_project'),
    # path('project/send_review/<str:encrypt_project_id>/', views.send_review, name='send_review'),
    # path('project/send_report/<str:encrypt_project_id>/', views.send_report, name='send_report'),
    # path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    # path('profile/change-password', views.change_password, name='change_password'),
]
