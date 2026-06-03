from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from author.api.serializer import AuthorSerializer
from author.models import Author


class AuthorView(GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author Successfully created"}, 201)
        return Response(serializer.errors, 422)


class AuthorUpdate(GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def put(self, request, pk):
        author = Author.objects.get(id=pk)
        data = request.data
        serializer = AuthorSerializer(author, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author successfully updated!!"}, 200)
        return Response(serializer.errors, 422)
