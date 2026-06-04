from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from librarian.models import Librarian
from librarian.api.serializer import LibrarianSerializer


class LibrarianView(GenericAPIView):

    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

    def get(self, request):
        librarians = Librarian.objects.all()
        serializer = LibrarianSerializer(librarians, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Librarian created successfully",
                    "employee_id": serializer.instance.employee_id,
                },
                status=201,
            )
        return Response(serializer.errors, status=422)


class LibrarianUpdateAndDelete(GenericAPIView):

    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

    def put(self, request, pk):
        librarian = get_object_or_404(Librarian, id=pk)
        serializer = LibrarianSerializer(librarian, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Librarian updated successfully"
                }, status=200)
        return Response(serializer.errors, status=422)

    def delete(self, request, pk):
        librarian = get_object_or_404(Librarian, id=pk)
        librarian.delete()
        return Response({
            "message": "Librarian deleted successfully"
            }, status=200)
