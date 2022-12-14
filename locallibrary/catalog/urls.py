from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
