from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from subscription.models import Subscription
from subscription.api.serializer import SubscriptionSerializer


# GET all + POST create
class SubscriptionView(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        if Subscription.objects.filter(plan_type=request.data.get("plan_type")).exists():
            return Response(
                {"error": "This plan already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SubscriptionSerializer(data=request.data)

        if serializer.is_valid():
            subscription = serializer.save()
            return Response(
                {
                'message': 'Plan type created successfully'
            },status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Update
class SubscriptionUpdate(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_object(self, pk):
        return get_object_or_404(Subscription, pk=pk)

    def put(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Plan type updated successfully'
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)