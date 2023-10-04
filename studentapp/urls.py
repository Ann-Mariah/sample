from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_details',views.add_details,name='add_details'),
    path('show_details',views.show_details,name='show_details'),
    path('updatepage/<int:pk>',views.updatepage,name='updatepage'),
    path('update_student_details/<int:pk>',views.update_student_details,name='update_student_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
]