from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/','django.contrib.auth.views.login',{"template_name":"login.html"},name='login'),
    url(r'logout/','django.contrib.auth.views.logout_then_login',{'login_url': '/'},name='logout'),
    
    url(r'', include('core.urls', namespace='core')),
    url(r'^funcionarios/', include('funcionarios.urls', namespace='funcionarios')),
    url(r'^materiais/', include('materiais.urls', namespace='materiais')),
    url(r'^servicos/', include('servicos.urls', namespace='servicos')),
    url(r'^vegetativo/', include('vegetativo.urls', namespace='vegetativo')),
    url(r'^usuarios/', include('usuarios.urls', namespace='usuarios')),
]
