from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicalPrescriptionSerializer
from .utils import generate_pdf
from django.http import FileResponse

class MedicalPrescriptionCreateAPIView(APIView): 
    def post(self, request):
        serializer = MedicalPrescriptionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            pdf_buffer = generate_pdf(serializer.data)
            
            response = FileResponse(pdf_buffer, as_attachment=True, filename='prescription.pdf')
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)