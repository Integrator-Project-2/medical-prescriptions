from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicalPrescriptionSerializer
from .utils import generate_pdf
from django.core.files.base import ContentFile

class MedicalPrescriptionCreateAPIView(APIView): 
    def post(self, request):
        serializer = MedicalPrescriptionSerializer(data=request.data)
        
        if serializer.is_valid():
            prescription = serializer.save()
            
            pdf_content = generate_pdf(serializer.data)
            
            prescription.prescription_file.save(
                f'prescription_{prescription.id}.pdf',
                ContentFile(pdf_content),
                save=True
            ) 
                       
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)