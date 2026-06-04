from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from membership.models import Membership
from membership.api.serializer import MembershipSerializer


# GET all memberships + POST membership
class MembershipView(GenericAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            membership = serializer.save()
            return Response({"message": "Membership registered successfully"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PUT + DELETE
class MembershipUpdateAndDelete(GenericAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def put(self, request, pk):
        membership = Membership.objects.get(id=pk)
        serializer = MembershipSerializer(membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Membership updated successfully"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        membership = Membership.objects.filter(id=pk)
        membership.delete()

        return Response(
            {"message": "Membership deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
