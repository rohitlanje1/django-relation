from .views import add_course_view,show_course_view,update_course_view,delete_course_view,add_stud_view,show_stud_view,update_stud_view,delete_stud_view
from django.urls import path

urlpatterns=[
    path("addc/",add_course_view,name="add_course_url"),
    path("showc/",show_course_view,name="show_course_url"),
    path("updtc/<int:pk>/",update_course_view,name="update_course_url"),
    path("delc/<int:pk>/",delete_course_view,name="delete_course_url"),

    path("asv/",add_stud_view,name="add_stud_url"),
    path("ssv/",show_stud_view,name="show_stud_url"),
    path("upsv/<int:pk>/",update_stud_view,name="update_stud_url"),
    path("delsv/<int:pk>/",delete_stud_view,name="delete_stud_url"),

]