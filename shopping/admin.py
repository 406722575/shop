from django.contrib import admin
from .models import ProductCategory,Productlist

# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display =  ['id','名称','描述', '图片']

admin.site.register(ProductCategory,ProductCategoryAdmin)


class ProductlistAdmin(admin.ModelAdmin):
    list_display =  ['id','名称','图片', '所属类别','价格','库存','已上架','创建时间','修改时间']
    list_editable = ['名称','所属类别','价格','库存','已上架']
    list_per_page = 2

admin.site.register(Productlist,ProductlistAdmin)