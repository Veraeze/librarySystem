from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='book')
router.register('authors', views.AuthorViewSet, basename='author')

review_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
review_router.register('reviews', views.ReviewViewSet, basename='review')

urlpatterns = router.urls + review_router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('books/', views.BookList.as_view(), name='books'),
#     # path('authors/', views.AuthorList.as_view(), name='authors'),
#     # path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
#     # path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
#
# ]