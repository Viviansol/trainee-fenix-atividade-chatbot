
from inventory import Inventory
from product import Product
from cart import Cart
from chatbotApp import Chatbot

if __name__ == '__main__':
    test_pen = Product("Pen", 2.50)

    test_inventory = Inventory()
    test_inventory.addProduct(test_pen, 44)

    test_cart = Cart(test_inventory)
    test_chatbot = Chatbot(test_inventory)
    test_chatbot.run()
