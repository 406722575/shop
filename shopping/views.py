from django.shortcuts import render, get_object_or_404
from .models import ProductCategory,Productlist

# Create your views here.
def home(request):
    all_Category = ProductCategory.objects.all()
    CategoryAndProducts = []
    for Eachcategory in all_Category:
        CategoryAndProducts.append((Eachcategory, Productlist.objects.filter(所属类别=Eachcategory, 已上架=True)[:1]))
    content = {"类别与商品": CategoryAndProducts, "所有类别":all_Category}
    return render(request,'shopping/home.html', content)

def SampleCategory(request, 每个类别_id):
    all_Category = ProductCategory.objects.all()
    all_need_Category =get_object_or_404(ProductCategory, id=每个类别_id)
    CategoryAndProducts = [(all_need_Category, Productlist.objects.filter(所属类别=all_need_Category, 已上架=True)[:2])]
    content = {"类别与商品": CategoryAndProducts, "所有类别":all_Category}
    return render(request,'shopping/home.html', content)

def detail(request, 每个类别_id, 每个商品_id):
    all_Category = ProductCategory.objects.all()
    Product =get_object_or_404(Productlist, id=每个商品_id ,已上架=True)
    content = {"商品": Product, "所有类别":all_Category}
    return render(request,'shopping/detail.html', content)