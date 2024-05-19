from urllib import request


class Cart:

    def __init__(self):
        self.request = request
        self.session = request.session

        cart = self.session.get("cart")
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, producto, cantidad):
        pass

    def delete(self, producto):
        pass

    def clear(self):
        pass

    def save(self):
        pass
# debo comenzar del modulo 3.2 desde cero
