"""hh_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import vacancy_details, vacancy_list, vacancy_details, top_vacancies, priority, \
    active, non_active, company_list, company_details, sorted_vacancies


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', company_list),
    path('api/companies/<int:company_id>/', company_details),
    path('api/companies/<int:companies_id>/vacancies/', sorted_vacancies),
    path('api/vacancies/', vacancy_list),
    path('api/vacancies/<int:vacancy_id>/', vacancy_details),
    path('api/vacancies/top_ten/', top_vacancies),
    path('api/vacancies/priority', priority),
    path('api/vacancies/active', active),
    path('api/vacancies/non_active', non_active)

]
