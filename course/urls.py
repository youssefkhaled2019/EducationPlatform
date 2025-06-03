from django.urls import path
from .  import views
app_name='course'
urlpatterns = [
        path('', views.subject_courses_list,name="subject_courses_list"),
        path('course/<slug:slug>/', views.course_detail, name='course_detail'),
        path('course/add-course', views.add_course, name='add_course'),
        path('course/edit-coures/<slug:slug>/', views.edit_course, name='edit_course'),
        path('course/<slug:slug>/add-module/', views.add_module, name='add_module'),
        path('course/enroll-course/<slug:slug>/', views.enroll_course, name='enroll_course'),
]
# course:enroll_course