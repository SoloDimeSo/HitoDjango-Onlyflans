
from django.contrib import admin
from django.urls import include, path
from web.views import contac_view, contac_view_exito, flan_details, index, about, welcome, compra_exito


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index, name='index'),
    path('about/', about, name='nosotros'),
    path('welcome/', welcome, name='bienvenidos'),
    path('contacto_exitoso/', contac_view_exito, name='contacto_exitoso'),
    path('contact_form/', contac_view, name='contacto'),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('flan/<int:flan_id>/' , flan_details, name='flan_details'),
    path('compra_exito/', compra_exito, name= 'gracias_compra')
]
