from product import Product
import json


class Inventory:
    def __init__(self):
        self.__products: dict = dict()

    def addProduct(self, product: Product, quantity: int) -> None:
        product_name = product.getProductName()
        product_quantity = self.__products.setdefault(product_name, \
                                                      [product, 0])

        product_quantity[1] += quantity
        self.__products[product_name] = product_quantity

    def addMultipleProducts(self, products: list) -> None:
        for product, quantity in products:
            self.addProduct(product, quantity)

    def removeProduct(self, product_name: str, quantity: int) -> bool:
        if product_name not in self.__products:
            print(f"{product_name}")
            return False

        product_quantity = self.__products[product_name]
        final_quantity = product_quantity[1] - quantity

        if final_quantity < 0:
            print(
                f"Impossível remover {quantity} {product_name}, porque existem apenas {product_quantity[1]} disponíveis")
            return False
        elif final_quantity == 0:
            del self.__products[product_name]
            return True
        elif final_quantity > 0:
            self.__products[product_name] = [product_quantity[0], \
                                             final_quantity]
            return True
        return False

    def removeMultiple(self, products: list) -> bool:
        remove_results = []
        for product_name, quantity in products:
            result = self.removeProduct(product_name, quantity)
            remove_results.append(result)
        return all(remove_results)

    def getProducts(self) -> dict:
        return self.__products

    def isAvailable(self, product_name, asked_quantity) -> bool:
        if product_name not in self.__products:
            print(f"Não temos {product_name}")
            return False

        product, available_quantity = self.__products[product_name]
        if asked_quantity > available_quantity:
            print(f"Temos apenas {available_quantity} disponíveis")
            return False

        return True

    def hasProduct(self, product_name: str) -> bool:
        return product_name in self.__products

    def __parse(self) -> str:
        parsed_products = dict()
        for product, quantity in self.__products.values():
            parsed_products[quantity] = product.parse()
        return json.dumps(parsed_products)

    def persist(self) -> None:
        with open("inventory.json", "w") as file:
            file.write(self.__parse())

    def load(self) -> None:
        with open("inventory.json", "r") as file:
            parsed_stock = json.load(file)
            for quantity, parsed_product in parsed_stock.items():
                quantity = int(quantity)
                product = Product.unparse(parsed_product)
                self.__products[product.getName()] = [product, quantity]

    def getPriceFor(self, product_name: str):
        if product_name in self.__products:
            return self.__products[product_name][0].getPrice()

