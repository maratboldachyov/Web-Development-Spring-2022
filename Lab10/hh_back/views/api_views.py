# from django.shortcuts import render
# from api.models import Vacancy, Company
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
#
# from django.views import View
# from django.http import HttpResponse

# @csrf_exempt
# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         companies_json = [company.to_json() for company in companies]
#         return JsonResponse(companies_json, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         try:
#             company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'], address=data['address'])
#         except Exception as e:
#             return JsonResponse({'message': str(e)})
#         return JsonResponse(company.to_json())
#
# @csrf_exempt
# def vacancy_list(request):
#     if request.method == 'GET':
#         vacancies = Vacancy.objects.all()
#         vacancy_json = [vacancy.to_json() for vacancy in vacancies]
#         return JsonResponse(vacancy_json, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         try:
#             vacancy = Vacancy.objects.create(name=data['name'], company_id=data['company_id'], salary=data['salary'], description=data['description'], active=data['active'], priority=data['priority'])
#         except Exception as e:
#             return JsonResponse({'message': str(e)})
#         return JsonResponse(vacancy.to_json())
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
#         company.name = data['name']
#         company.description = data['description']
#         company.city = data['city']
#         company.address = data['address']
#         company.save()
#         return JsonResponse(company.to_json())
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
#         vacancy.name = data['name']
#         vacancy.description = data['description']
#         vacancy.salary = data['salary']
#         vacancy.priority = data['priority']
#         vacancy.active = data['active']
#         vacancy.company_id = data['company_id']
#         vacancy.save()
#         return JsonResponse(vacancy.to_json())
#
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

