from django.urls import path 
from .views import BookAPIView, CreateAPIBook, CrudAPIBook, UsersAPIDetail, UsersAPIList, UserViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter 

urlpatterns = [

    path('', BookAPIView.as_view()),
    path('create', CreateAPIBook.as_view()),
    path('<int:pk>/', CrudAPIBook.as_view()),
    # path('users/', UsersAPIList.as_view()),
    # path('users/<int:pk>/', UsersAPIDetail.as_view()),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls