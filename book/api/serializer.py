from rest_framework import serializers
from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    # 👇 READABLE OUTPUT FIELDS
    authors_name = serializers.StringRelatedField(
        source='authors',
        many=True,
        read_only=True
    )

    categories_name = serializers.StringRelatedField(
        source='categories',
        many=True,
        read_only=True
    )

    publisher_name = serializers.StringRelatedField(
        source='publisher',
        read_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'isbn',

            # writable (IDs)
            'authors',
            'categories',
            'publisher',

            # readable (names)
            'authors_name',
            'categories_name',
            'publisher_name',

            'published_date',
            'total_copies',
            'available_copies',
            'description',
            'cover_image',
            'is_active',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        total = data.get('total_copies', 1)
        available = data.get('available_copies', 1)

        if available > total:
            raise serializers.ValidationError(
                "Available copies cannot be greater than total copies."
            )

        return data