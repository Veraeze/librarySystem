from rest_framework import serializers

from catalogue.models import Book, Author, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#
#     class Meta:
#         model = Book
#         fields = ['title', 'summary', 'isbn', 'author']
#
class BookSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author_detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'name', 'date', 'message']

    def create(self, validated_data):
        book_pk = self.context['book_pk']
        return Review.objects.create(book_id=book_pk, **validated_data)

