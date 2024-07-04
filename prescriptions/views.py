from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicalPrescriptionSerializer

class MedicalPrescriptionCreateAPIView(APIView): 
    def post(self, request):
        serializer = MedicalPrescriptionSerializer
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)