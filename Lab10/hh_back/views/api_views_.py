# from django.shortcuts import render
# from api.models import Vacancy, Company
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
#
# from django.views import View
# from django.http import HttpResponse
# from api.serializers import CompanySerializer, CompanySerializer2, VacancySerializer
#
#
# @csrf_exempt
# def company_list(request):
#     if request.method == 'GET':
#         # companies = Company.objects.filter(name_contains='').order_by('-id')
#         companies = Company.objects.all()
#         serializer = CompanySerializer2(companies, many=True)
#         # companies_json = [company.to_json() for company in companies]
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         # try:
#         #     company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'], address=data['address'])
#         # except Exception as e:
#         #     return JsonResponse({'message': str(e)})
#         serializer = CompanySerializer2(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#
# @csrf_exempt
# def vacancy_list(request):
#     if request.method == 'GET':
#         vacancies = Vacancy.objects.all()
#         # vacancy_json = [vacancy.to_json() for vacancy in vacancies]
#         serializer = VacancySerializer(vacancies, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         # try:
#         #     vacancy = Vacancy.objects.create(name=data['name'], company_id=data['company_id'], salary=data['salary'], description=data['description'], active=data['active'], priority=data['priority'])
#         # except Exception as e:
#         #     return JsonResponse({'message': str(e)})
#         serializer = VacancySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#
# @csrf_exempt
# def company_details(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'message'}, str(e), status=400)
#     if request.method == 'GET':
#         return JsonResponse(company.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         # company.name = data['name']
#         # company.description = data['description']
#         # company.city = data['city']
#         # company.address = data['address']
#         # company.save()
#         serializer = CompanySerializer(instance=company, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         # return JsonResponse(company.to_json())
#         return JsonResponse(serializer.errors)
#     elif request.method == "DELETE":
#         company.delete()
#         return JsonResponse({'message': 'deleted'}, status=204)
#
#
# @csrf_exempt
# def vacancy_details(request, vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id=vacancy_id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'message'}, str(e), status=400)
#     if request.method == 'GET':
#         return JsonResponse(vacancy.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         # vacancy.name = data['name']
#         # vacancy.description = data['description']
#         # vacancy.salary = data['salary']
#         # vacancy.priority = data['priority']
#         # vacancy.active = data['active']
#         # vacancy.company_id = data['company_id']
#         # vacancy.save()
#         serializer = VacancySerializer(instance='name', data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     elif request.method == 'DELETE':
#         vacancy.delete()
#         return JsonResponse({'message': 'deleted'}, status=204)
#
# def top_vacancies(request):
#     vacancy_ordered = Vacancy.objects.order_by('-salary')[:10]
#     vacancy_ordered_to_json = [item.to_json() for item in vacancy_ordered]
#     return JsonResponse(vacancy_ordered_to_json, safe=False)
#
#
# def sorted_vacancies(request, companies_id):
#     try:
#         vacancies = Vacancy.objects.filter(company=companies_id)
#         vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
#     except Company.DoesNotExist as e:
#         return JsonResponse({'message'}, str(e), status=400)
#     return JsonResponse(vacancies_to_json, safe=False)
#
#
# def priority(request):
#     vacancy_ordered = Vacancy.objects.order_by('-priority')
#     vacancy_ordered_to_json = [item.to_json() for item in vacancy_ordered]
#     return JsonResponse(vacancy_ordered_to_json, safe=False)
#
#
# def active(request):
#     try:
#         vacancies = Vacancy.objects.filter(active=True)
#         vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
#     except Company.DoesNotExist as e:
#         return JsonResponse({'message'}, str(e), status=400)
#     return JsonResponse(vacancies_to_json, safe=False)
#
#
# def non_active(request):
#     try:
#         vacancies = Vacancy.objects.filter(active=False)
#         vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
#     except Company.DoesNotExist as e:
#         return JsonResponse({'message'}, str(e), status=400)
#     return JsonResponse(vacancies_to_json, safe=False)
#
#
