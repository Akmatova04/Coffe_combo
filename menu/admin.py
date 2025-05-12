from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Аталышын жазганда слаг автоматтык түрдө толтурулат

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_special')
    list_filter = ('category', 'is_special')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_special') # Админден тизмеде туруп эле баасын/өзгөчөлүгүн өзгөртүүгө