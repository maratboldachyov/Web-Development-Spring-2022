from django.http import JsonResponse
from django.shortcuts import render
from api.models import Category, Product


def Products_List(request):
    products = Product.objects.all()
    products_json = [product.JSON_Format() for product in products]
    return JsonResponse(products_json, safe=False)


def Categories_List(request):
    categories = Category.objects.all()
    categories_json = [category.JSON_Format() for category in categories]
    return JsonResponse(categories_json, safe=False)


def Product_Details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(product.JSON_Format())


def Category_Details(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(category.JSON_Format())


def Sorted_Products(request, category_id):
    try:
        products = Product.objects.filter(category=category_id)
        products_json = [product.JSON_Format() for product in products]
    except Category.DoesNotExist as e:
        return JsonResponse({'message'}, str(e), status=400)
    return JsonResponse(products_json, safe=False)
