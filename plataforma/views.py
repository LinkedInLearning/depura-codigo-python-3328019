from django.http import JsonResponse
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Categoria, DetalleFactura, Producto, Cliente, Factura, Empleado, Departamento
from .serializers import CategoriaSerializer, DetalleFacturaSerializer, ProductoSerializer, ClienteSerializer, FacturaSerializer, EmpleadoSerializer, DepartamentoSerializer


class CategoriaViewSet(ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoViewSet(ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DepartamentoViewSet(ReadOnlyModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
class EmpleadoViewSet(ReadOnlyModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class FacturaViewSet(ReadOnlyModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class DetalleFacturaViewSet(ReadOnlyModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer
