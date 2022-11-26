# -*- coding: utf-8 -*-
from unidecode import unidecode


class Product:
    def __init__(self, name: str, price: float):
        self.__name: str = Product.__cleanName(name)
        self.__price: float = price

    @staticmethod
    def __cleanName(name: str) -> str:
        name = unidecode(name)
        return name.strip().lower().replace(" ", "")

    def getProductName(self) -> str:
        return self.__name

    def getProductPrice(self) -> float:
        return self.__price

    def parseProduct(self) -> list:
        return [self.__name, self.__price]

    def getPrice(self) -> float:
        return self.__price

    @staticmethod
    def unparse(parsed_product: str):
        try:
            name = parsed_product[0]
            price = parsed_product[1]
        except:
            raise ValueError(f"Erro ao fazer unparse de: {parsed_product}")
        return Product(name, price)
