from unidecode import unidecode
from cart import Cart
from inventory import Inventory
import re


class Chatbot:
    __menu = "=" * 50
    __menu += "\nBem vindo ao Chatbot de atendimento!! :)"
    __menu += "\nOs seguintes comandos estão disponíveis:"
    __menu += "\n1- Adicionar item"
    __menu += "\n2- Remover item"
    __menu += "\n3- Mostrar carrinho"
    __menu += "\n4- Fechar carrinho de compras\n"
    __menu += "=" * 50

    __open_cart = True

    def __init__(self, inventory: Inventory):
        self.__cart = Cart(inventory)

    def run(self):
        Chatbot.__open_cart = True
        self.__cart.resetCart()
        while self.__open_cart:
            print(self.__menu)
            command = self.__receiveInput()
            if command == "1":
                self.__add()
            elif command == "2":
                self.__remove()
            elif command == "3":
                self.__showCart()
            elif command == "4":
                self.__closeCart()

    def __receiveInput(self):
        user_input = str(input("Sua escolha:"))
        user_input = unidecode(user_input)
        print()
        print("=" * 50)
        return user_input.strip().lower().replace(" ", "")

    def __productAndQuantityFromInput(self, user_input: str) -> bool:
        quantity_pattern = "[^-0-9]*(-*\d*)[^-0-9]*"
        product_pattern = "[-0-9]*([a-z]*)[-0-9]*"

        quantity = -1
        try:
            quantity = int(re.search(quantity_pattern, user_input)[1])
        except:
            pass
        product_name = re.search(product_pattern, user_input)[1]

        return (product_name, quantity)

    def __validateNameAndQuantity(self, name: str, quantity: int) -> bool:
        if name == "":
            print("Por favor informe o nome do produto")
            return False
        if quantity <= 0:
            print("Por favor insira uma quantidade válida")
            return False
        return True

    def __add(self):
        print()
        print("Ótimo! Informe o produto desejado e a quantidade a adicionar :)")
        user_input = self.__receiveInput()

        product_name, quantity = self.__productAndQuantityFromInput(user_input)
        if self.__validateNameAndQuantity(product_name, quantity):
            # tudo valido
            self.__cart.add(product_name, quantity)
            print("Deseja adicionar mais algum produto? S/N")

            user_input = self.__receiveInput()
            if user_input == "s":
                self.__add()
        else:
            self.__add()
            pass

    def __remove(self):
        print()
        print("Ótimo! Informe o produto desejado e a quantidade a remover :)")
        user_input = self.__receiveInput()

        product_name, quantity = self.__productAndQuantityFromInput(user_input)
        if self.__validateNameAndQuantity(product_name, quantity):
            # tudo valido
            self.__cart.remove(product_name, quantity)
            print("Deseja remover mais algum produto? S/N")

            user_input = self.__receiveInput()
            if user_input == "s":
                self.__remove()
        else:
            # entrada invalida
            self.__remove()
            pass

    def __showCart(self):
        products = self.__cart.getProducts()
        for product_name, quantity in products.items():
            print(f"-{quantity}x {product_name}(s)")

    def __closeCart(self):
        print()
        total_price = self.__cart.closeCart()
        print("Sua compra foi finalizada!")
        print(f"O preço total foi R${total_price}")
        print("Obrigado pela preferência!")
        Chatbot.__open_cart = False
