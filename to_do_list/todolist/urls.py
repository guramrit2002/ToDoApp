from django.urls import path
from . import views
urlpatterns = [
    path('',views.getNotes),
    path('notes/<int:pk>',views.getNote),
    path('notes/create',views.createnote),
    path('notes/<int:pk>/update',views.updatenote),
    path('notes/<int:pk>/delete',views.deletenote),
]
