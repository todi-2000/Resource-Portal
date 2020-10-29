from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.home,name='home'),
    path('editform/',views.ProfileEditForm,name='editform'),
    path('upload/resource',views.uploadresources,name='resource'),
    path('index',views.index,name='index'),
    path('resource',views.resources,name='resources'),
    path('books',views.books,name='books'),
    path('byteachers',views.teachers,name='byteacher'),
    path('favourites',views.saved,name='saved'),
    path('delete',views.deleteresource,name='delete')
]
