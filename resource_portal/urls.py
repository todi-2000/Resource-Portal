from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.home,name='home'),
    path('editform/',views.ProfileEditForm,name='editform')
]