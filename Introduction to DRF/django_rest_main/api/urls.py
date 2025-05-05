from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register('employees',views.EmployeesViewSet,basename='employee')

urlpatterns = [

    path('students/',views.studentsView),
    path('students/<int:id>/',views.studentDetailView),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:id>/',views.EmployeeDetail.as_view()),

    path('',include(router.urls)),

    path('products/',views.Products.as_view()),
    path('products/<int:id>/',views.ProductDetail.as_view()),

    path('posts/',views.Posts.as_view()),
    path('posts/<int:id>',views.PostDetail.as_view()),


    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),

    path('blogs/<int:id>/',views.BlogDetailView.as_view()),
    path('comments/<int:id>/',views.CommentDetailView.as_view()),

]
