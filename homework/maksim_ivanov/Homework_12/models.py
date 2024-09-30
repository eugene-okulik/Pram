from typing import List, Optional, TypeVar


class Flower:
    def __init__(self, name: str, color: str, life_time: int, stem_length: int, price: float):
        self.__name: str = name
        self.__color: str = color
        self.__life_time: int = life_time
        self.__stem_length: int = stem_length
        self.__price: float = price

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def life_time(self):
        return self.__life_time

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return (f"{self.__name}, {self.__color}. Цена: {self.__price} р., время жизни: {self.__life_time} д., "
                f"длина стебля: {self.__stem_length} см.")


class Rose(Flower):
    def __init__(self, color: str, stem_length: int, price: float):
        super().__init__("Роза", color, 10, stem_length, price)


class Lily(Flower):
    def __init__(self, color: str, stem_length: int, price: float):
        super().__init__("Лилия", color, 8, stem_length, price)


class Peony(Flower):
    def __init__(self, color: str, stem_length: int, price: float):
        super().__init__("Пион", color, 11, stem_length, price)


class Chrysanthemum(Flower):
    def __init__(self, color: str, stem_length: int, price: float):
        super().__init__("Хризантема", color, 13, stem_length, price)


FlowerType = TypeVar('FlowerType', bound=Flower)


class Bouquet:
    def __init__(self, flowers: Optional[List[FlowerType]] = None):
        if flowers is None:
            flowers = []
        self.__flowers: List[FlowerType] = flowers

    @property
    def cost(self):
        return sum(flover.price for flover in self.__flowers)

    @property
    def average_life_time(self):
        if len(self.__flowers) == 0:
            return 0
        else:
            return round(sum([flover.life_time for flover in self.__flowers]) / len(self.__flowers), 1)

    def add_flower(self, flover: FlowerType):
        self.__flowers.append(flover)

    def sort_by(self, parameter, reverse=False):
        if not self.__flowers:
            return []
        sorted_flowers = sorted(self.__flowers, key=lambda x: getattr(x, parameter), reverse=reverse)
        return sorted_flowers

    def sorted_by_name(self, reverse=False):
        return self.sort_by('name', reverse)

    def sorted_by_color(self, reverse=False):
        return self.sort_by('color', reverse)

    def sorted_by_life_time(self, reverse=False):
        return self.sort_by('life_time', reverse)

    def sorted_by_stem_length(self, reverse=False):
        return self.sort_by('stem_length', reverse)

    def sorted_by_price(self, reverse=False):
        return self.sort_by('price', reverse)

    def search_by(self, parameter, value):
        if not self.__flowers:
            return []
        found_flowers = []
        for flower in self.__flowers:
            attr_value = getattr(flower, parameter)
            if isinstance(value, str):
                if value.lower() in attr_value.lower():
                    found_flowers.append(flower)
            else:
                if value == attr_value:
                    found_flowers.append(flower)
        return found_flowers

    def __str__(self):
        if not self.__flowers:
            return ''
        all_flowers = [str(flower) for flower in self.__flowers]
        return "\n".join(all_flowers)
