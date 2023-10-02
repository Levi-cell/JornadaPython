from requests import get, post, delete
from json import loads, dumps

# ('https://private-anon-0abfd38802-pizzaapp.apiary-mock.com/restaurants/restaurantId/menu?category=Pizza&orderBy=rank')
# "https://private-anon-0abfd38802-pizzaapp.apiary-mock.com/orders/"

fila_de_pedidos = get('https://private-anon-fa678dd7ad-pizzaapp.apiary-mock.com/orders/id')

orders = loads(fila_de_pedidos.text)
print(orders)

# MENU

cardapio = get('https://private-anon-fa678dd7ad-pizzaapp.apiary-mock.com/restaurants/restaurantId/menu?category=Pizza&orderBy=rank')
print(cardapio.text)

# PEDIDO

pedido = {"cart": [
    {
        "menuItemId": 2,
        "quantity": 1
    },
    {
        "menuIemID": 3,
        "quantity": 1
    },
],
    "resturantId": 1
}

pedidoEnviado = post("https://private-anon-fa678dd7ad-pizzaapp.apiary-mock.com/orders/", data=dumps(pedido))

print(pedidoEnviado)
loads(pedidoEnviado.text)

print(pedidoEnviado)
