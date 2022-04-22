from django.shortcuts import render
from api.models import Vacancy, Company
from django.http import JsonResponse
import operator


def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)


def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(company.to_json())


def vacancy_details(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(vacancy.to_json())


def top_vacancies(request):
    vacancy_ordered = Vacancy.objects.order_by('-salary')[:10]
    vacancy_ordered_to_json = [item.to_json() for item in vacancy_ordered]
    return JsonResponse(vacancy_ordered_to_json, safe=False)


def sorted_vacancies(request, companies_id):
    try:
        vacancies = Vacancy.objects.filter(company=companies_id)
        vacancies_tojson = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(vacancies_tojson, safe=False)


def priority(request):
    vacancy_ordered = Vacancy.objects.order_by('-priority')
    vacancy_ordered_to_json = [item.to_json() for item in vacancy_ordered]
    return JsonResponse(vacancy_ordered_to_json, safe=False)


def active(request):
    try:
        vacancies = Vacancy.objects.filter(active=True)
        vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(vacancies_to_json, safe=False)


def non_active(request):
    try:
        vacancies = Vacancy.objects.filter(active=False)
        vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(vacancies_to_json, safe=False)


