"""
URL configuration for AI_SAS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from anonymous import views as anoview
from django.conf import settings
from django.conf.urls.static import static
from student import views as stdview
from faculty import views as facview


urlpatterns = [
    path('admin/', admin.site.urls),
    # student page
    path('studentdashboard/',stdview.studentdashboard,name='studentdashboard'),
    path('studentexam/',stdview.studentexam,name='studentexam'),
    path('studentlogout/',stdview.studentlogout,name='studentlogout'),
    path('studentprofile/',stdview.studentprofile,name='studentprofile'),
    path('studentresult/',stdview.studentresult,name='studentresult'),
    path('studentchangepwd/',stdview.studentchangepwd,name='studentchangepwd'),
    path('studentvideo/',stdview.studentvideo,name='studentvideo'),
    path('videos_display/',stdview.videos_display,name='videos_display'),


# faculty page
    path('add-question/',facview.add_question,name='add_question'),
    path('facultydashboard/',facview.facultydashboard,name='facultydashboard'),
    path('facultyprofile/',facview.facultyprofile,name='facultyprofile'),
    path('facultyresult/',facview.facultyresult,name='facultyresult'),
    path('facultylogout/',facview.facultylogout,name='facultylogout'),
    path('facultychangepwd/',facview.facultychangepwd,name='facultychangepwd'),
    path('facultyvideo/',facview.facultyvideo,name='facultyvideo'),
    path('studentlist/',facview.studentlist,name='studentlist'),


    


    # Home page
    path('', anoview.index, name='index'),
    path('index/', anoview.index),
    path('home/', anoview.index),

    # Static pages
    path('about/', anoview.about, name='about'),
    path('contact/', anoview.contact, name='contact'),
    path('gallery/', anoview.gallery, name='gallery'),
    path('faq/', anoview.faq, name='faq'),
    path('users/', anoview.users, name='users'),
    path('update/', anoview.update, name='update'),
    path('api/',anoview.EmployeeView.as_view()),
    path('api/<int:id>/',anoview.EmployeeView.as_view()),

    # Authentication
    path('login/', anoview.login, name='login'),
    path('register/', anoview.register, name='register'),

    # Dashboard
    path('dashboard/', anoview.dashboard, name='dashboard'),
    path('project/', anoview.project_view, name='project'),
    path('project/delete/<int:pk>/', anoview.project_delete, name='project_delete'),  # delete project
    path('course/', anoview.course, name='course'),
    path('development/', anoview.development, name='development'),

    # Tools
    path('calculator/', anoview.calculator, name='calculator'),

    # AI Chat Assistant
    path('chat/', anoview.chat_page, name='chat_page'),
    path('chat/response/', anoview.chat_response, name='chat_response'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
