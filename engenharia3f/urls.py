from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls', namespace='core')),
    url(r'^funcionarios', include('funcionarios.urls', namespace='funcionarios')),
    url(r'^materiais', include('materiais.urls', namespace='materiais')),
]
