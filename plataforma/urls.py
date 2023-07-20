from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet,
    DetalleFacturaViewSet,
    ProductoViewSet,
    ClienteViewSet,
    FacturaViewSet,
    EmpleadoViewSet,
    DepartamentoViewSet,
)

router = DefaultRouter()
router.register("categorias", CategoriaViewSet)
router.register("clientes", ClienteViewSet)
router.register("facturas", FacturaViewSet)
router.register("detalle_factura", DetalleFacturaViewSet)
router.register("empleados", EmpleadoViewSet)
router.register("departamentos", DepartamentoViewSet)

urlpatterns = []
