from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.

"""vista para catalogo de productos"""


def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos': listaProductos,
        'categorias': listaCategorias
    }
    print(listaProductos)
    return render(request, 'index.html', context)


def productosPorCategoria(request, categoria_id):
    """vista para filtrar productos por categoria"""
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    return render(request, 'index.html', context)


def productosPorNombre(request):
    """ vista para filtrado de productos por nombre """
    nombre = request.POST['nombre']

    listaProductos = Producto.objects.filter(nombre__contains=nombre)
    listaCategorias = Categoria.objects.all()

    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }

    return render(request, 'index.html', context)
