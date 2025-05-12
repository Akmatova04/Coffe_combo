from django.urls import path
from . import views

urlpatterns = [
    # Башкы бет (мисалы, өзгөчө сунуштарды көрсөтөт)
    path('', views.home_view, name='home'),
    # Толук меню барагы
    path('menu/', views.menu_view, name='menu_list'),
    # Келечекте ар бир элементтин өзүнчө барагы үчүн (керек болсо):
    # path('item/<slug:item_slug>/', views.menu_item_detail, name='menu_item_detail'),
]