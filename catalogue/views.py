from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from catalogue.models import Book, Author, Review
from catalogue.pagination import DefaultPagination
from catalogue.serializers import BookSerializer, AuthorSerializer, ReviewSerializer
import segno
from rest_framework.permissions import IsAuthenticated


# Class view set
class BookViewSet(ModelViewSet):
    pagination_class = DefaultPagination

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name']


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_pk': self.kwargs['book_pk']}
        # key word argument = kwargs

# Class based views
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# Function based views
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# # the response class returns serialized data
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, id=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         author_orcode = segno.make_qr("message")
#         author_orcode.save("message.png")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
