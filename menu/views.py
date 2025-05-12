from django.shortcuts import render
from .models import Category, MenuItem

def menu_view(request):
    # Бардык категорияларды жана аларга тиешелүү активдүү меню элементтерин алабыз
    categories = Category.objects.prefetch_related('items').all()
    special_items = MenuItem.objects.filter(is_special=True)

    context = {
        'categories': categories,
        'special_items': special_items,
        'page_title': "Биздин Меню", # Баракчанын аталышы үчүн
    }
    return render(request, 'menu/menu_list.html', context)

def home_view(request):
    # Башкы бет үчүн, мисалы, өзгөчө сунуштарды гана көрсөтүү
    special_items = MenuItem.objects.filter(is_special=True)
    context = {
        'special_items': special_items,
        'page_title': "Башкы бет",
    }
    # Башкы бет үчүн өзүнчө шаблон же меню шаблонун колдонсо болот
    return render(request, 'menu/home.html', context) # home.html түзүш керек