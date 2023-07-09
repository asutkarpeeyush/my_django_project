from django.urls import path
from . import views


urlpatterns = [
    # No matter what the HTTP request is (GET/POST/PUT/PATCH), invoke the same view.
    path('list_books/<int:id>/', views.book, {"name": "Piyush"}),
    path('list_books', views.ListBooks.as_view(), {"name": "Piyush"}),
    path('my_view', views.my_view),
    path('', views.dummy_view)
]
