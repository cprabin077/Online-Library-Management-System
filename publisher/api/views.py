from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from publisher.api.serializer import PublisherSerializer
from publisher.models import Publisher


class PublisherView(GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get(self, request):
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Publisher Successfully created"}, 201)
        return Response(serializer.errors, 422)


class PublisherUpdateAndDelete(GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def put(self, request, pk):
        publisher = Publisher.objects.get(id=pk)
        data = request.data
        serializer = PublisherSerializer(publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Publisher successfully updated!!"}, 200)
        return Response(serializer.errors, 422)
    
    def delete(self, request, pk):
        publisher = Publisher.objects.filter(id=pk)
        publisher.delete()
        return Response({
            'message': "Publisher successfully deleted !!"
        }, 200)
