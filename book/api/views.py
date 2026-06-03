from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from book.models import Book
from book.api.serializer import BookSerializer


class BookView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        books = Book.objects.all().order_by('-created_at')
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            # optional: auto-set available copies = total copies
            serializer.save(available_copies=serializer.validated_data.get('total_copies', 1))

            return Response(
                {"message": "Book successfully created"},
                status=201
            )

        return Response(serializer.errors, status=422)


class BookUpdateAndDelete(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Book successfully updated!!"},
                status=200
            )

        return Response(serializer.errors, status=422)

    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()

        return Response(
            {"message": "Book successfully deleted !!"},
            status=200
        )