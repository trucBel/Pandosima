from django.urls import path,include
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
urlpatterns = [
    path('', include('snippets.urls')),
]