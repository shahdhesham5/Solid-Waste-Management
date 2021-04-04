from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns=[
path("",CourseList.as_view(),name='course_list'),
path("/<int:pk>/",CourseDetail.as_view(),name='CourseDetail'),
path("/create",CourseCreate.as_view(),name='addcourse'),
path("/update/<int:pk>",CourseUpdate.as_view(),name='updatecourse'),
path("/delete/<int:pk>",CourseDelete.as_view(),name='deletecourse'),
path("/student/create",StudentCreate.as_view(),name='addstudent'),

path("/student/<int:pk>",StudentDetail.as_view(),name='studentDetail'),
path("/student/update/<int:pk>",StudentUpdate.as_view(),name='studentupdate'),
path("/student/new",student_signup_view,name='newstudent'),
path('/studentlogin', Login.as_view(),name='studentlogin'),

path('/enroll/<int:pk>', enroll,name='enroll'),
path('/unenroll/<int:pk>', unenroll,name='unenroll'),


path('/eval',eval,name='eval')

]
