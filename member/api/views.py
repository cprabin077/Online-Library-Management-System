from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from member.models import Member
from .serializer import MemberSerializer


class MemberView(GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Member created successfully",
                    "library_card": serializer.instance.library_card_no
                },
                status=201
            )

        return Response(serializer.errors, status=422)


class MemberDetailView(GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, pk):
        member = get_object_or_404(Member, id=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        member = get_object_or_404(Member, id=pk)
        serializer = MemberSerializer(member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Member updated successfully"}, status=200)

        return Response(serializer.errors, status=422)

    def delete(self, request, pk):
        member = get_object_or_404(Member, id=pk)
        member.delete()

        return Response({"message": "Member deleted successfully"}, status=200)