# from rest_framework.views import APIView
# from django.views import View
# from rest_framework.response import Response
# from rest_framework.request import Request
# from api.serializers import CompanySerializer2
# from api.models import Company
# from django.shortcuts import Http404
#
#
# class CompanyListAPIView(APIView):
#     def get(self, request):
#         companies = Company.objects.all()
#         serializer = CompanySerializer2(companies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CompanySerializer2(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
# class CompanyDetailsAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Company.objects.get(id=pk)
#         except Company.DoesNotExist as e:
#             raise Http404
#
#     def get(self, request, pk=None):
#         company = self.get_object(pk)
#         serializer = CompanySerializer2(company)
#         return Response(serializer.data)
#
#     def put(self, request, pk = None):
#         company = self.get_object(pk)
#         serializer = CompanySerializer2(instance=company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     def delete(self, instance, pk=None):
#         company = self.get_object(pk)
#         company.delete()
#         return Response({'message': 'deleted'}, status=204)
