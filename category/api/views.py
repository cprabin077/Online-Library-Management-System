from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from category.api.serializer import CategorySerializer
from category.models import Category


class CategoryView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category Successfully created"}, 201)

        return Response(serializer.errors, 422)


class CategoryUpdate(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def put(self, request, pk):
        category = Category.objects.get(id=pk)

        data = request.data

        serializer = CategorySerializer(category, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message": "Category successfully updated!!"}, 200)

        return Response(serializer.errors, 422)
