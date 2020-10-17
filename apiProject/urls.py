from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from cadastro.views import CadastroViewSet
from contrato.views import ContratoViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'cadastro', CadastroViewSet)
router.register(r'contrato', ContratoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('new/', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token)
]