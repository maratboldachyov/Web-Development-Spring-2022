# from rest_framework.decorators import api_view
# from api.models import Vacancy, Company
# from api.serializers import CompanySerializer, CompanySerializer2, VacancySerializer
# from rest_framework.request import Request
# from rest_framework.response import Response
# from django.http.request import HttpRequest
# from django.http.response import HttpResponse, JsonResponse
#
# @api_view(['GET', 'POST'])
# def company_list(request):
#     if request.method == 'GET':
#         # companies = Company.objects.filter(name_contains='').order_by('-id')
#         companies = Company.objects.all()
#         serializer = CompanySerializer2(companies, many=True)
#         # companies_json = [company.to_json() for company in companies]
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # data = json.loads(request.body) Due to API_VIEW we don't need this row
#         # try:
#         #     company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'], address=data['address'])
#         # except Exception as e:
#         #     return JsonResponse({'message': str(e)})
#         serializer = CompanySerializer2(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def company_details(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'message'}, str(e), status=400)
#     if request.method == 'GET':
#         return JsonResponse(company.to_json())
#     elif request.method == 'PUT':
#         # data = json.loads(request.body)
#         # company.name = data['name']
#         # company.description = data['description']
#         # company.city = data['city']
#         # company.address = data['address']
#         # company.save()
#         serializer = CompanySerializer2(instance=company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         # return JsonResponse(company.to_json())
#         return Response(serializer.errors)
#     elif request.method == "DELETE":
#         company.delete()
#         return Response({'message': 'deleted'}, status=204)
