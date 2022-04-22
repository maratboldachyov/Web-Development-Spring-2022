from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Company
from api.serializers import CompanySerializer2


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    permission_classes = (IsAuthenticated,)



class CompanyDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    # lookup_field = 'company_id'