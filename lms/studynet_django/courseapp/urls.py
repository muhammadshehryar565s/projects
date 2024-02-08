from django.urls import path
from courseapp import views

urlpatterns = [
    path('',views.get_courses),
    
    path('categorys/', views.get_categorys),
    path('<slug:slug>/',views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comment/',views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get_quiz/',views.get_quiz),
    path('<slug:course_slug>/<slug:lesson_slug>/display_comment/',views.get_comments),
    
    
    # path('<slug:course_slug>/<slug:lesson_slug>/show_comment/', views.get_comments),
]
