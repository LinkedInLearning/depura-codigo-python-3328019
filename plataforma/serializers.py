from rest_framework import serializers
from .models import (
    Categoria,
    DetalleFactura,
    Producto,
    Cliente,
    Factura,
    Empleado,
    Departamento,
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Producto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = "__all__"


class FacturaSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer()
    cliente = ClienteSerializer()

    class Meta:
        model = Factura
        fields = "__all__"


class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = "__all__"
