from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:id>/',views.studentDetailView),
    path('employees/',views.Employees.as_view()),
    path('employees/<int:id>/',views.EmployeeDetail.as_view()),
    path('products/',views.Products.as_view()),
    path('products/<int:id>',views.ProductDetail.as_view()),
]
