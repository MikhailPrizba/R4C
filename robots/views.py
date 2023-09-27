from rest_framework.views import APIView
from .serializers import RobotCreateSerializer
from rest_framework.response import Response
from rest_framework import status


class RobotCreateView(APIView):
    def post(self, request):
        serializer = RobotCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)