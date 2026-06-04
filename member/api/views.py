from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from member.models import Member
from member.api.serializer import MemberSerializer

class MemberView(GenericAPIView):

    serializer_class = MemberSerializer

    def get(self, request):

        members = Member.objects.all().order_by('-joined_at')
        serializer = MemberSerializer(members, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):

        serializer = MemberSerializer(data=request.data)

        if serializer.is_valid():

            member = serializer.save()

            return Response(
                {
                    "message": "Member registered successfully (pending approval)",
                    "member_id": member.id,
                    "library_card": member.library_card_no,
                    "qr_code": member.qr_code,
                    "is_active": member.is_active
                },
                status=201
            )

        return Response(serializer.errors, status=422)

# Member details view    
class MemberDetailView(GenericAPIView):

    serializer_class = MemberSerializer

    def get(self, request, pk):

        member = get_object_or_404(Member, id=pk)
        serializer = MemberSerializer(member)

        return Response(serializer.data, status=200)

    def put(self, request, pk):

        member = get_object_or_404(Member, id=pk)

        serializer = MemberSerializer(
            member,
            data=request.data,
            partial=True   # 🔥 IMPORTANT FIX
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Member updated successfully",
                    "is_active": member.is_active
                },
                status=200
            )

        return Response(serializer.errors, status=422)

    def delete(self, request, pk):

        member = get_object_or_404(Member, id=pk)
        member.delete()

        return Response(
            {"message": "Member deleted successfully"},
            status=200
        )

# member approve    
class MemberApproveView(GenericAPIView):

    def post(self, request, pk):

        member = get_object_or_404(Member, id=pk)

        # 🔥 APPROVAL STEP
        member.is_active = True
        member.save()

        return Response(
            {
                "message": "Member approved successfully",
                "member_id": member.id,
                "status": "ACTIVE"
            },
            status=200
        )