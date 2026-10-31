from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('loans/', views.loan_list, name='loan_list'), # <--- Новая страница
    path('issue/<int:book_id>/', views.issue_book, name='issue_book'),
    path('return/<int:loan_id>/', views.return_book, name='return_book'),
]