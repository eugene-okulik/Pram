from models import Rose, Lily, Peony, Chrysanthemum, Bouquet

flowers = [
    Rose("красный", 15, 99.5),
    Rose("красный", 20, 99.5),
    Rose("черный", 16, 99.5),
    Lily("белый", 10, 200),
    Peony("розовый", 15, 50),
    Peony("белый", 20, 50),
    Chrysanthemum("желтый", 20, 70)
]

bouquet = Bouquet(flowers)

bouquet.add_flower(Peony("красный", 25, 50))

print(f"Состав букета:\n{bouquet}")

print(f"Время увядания букета: {bouquet.average_life_time} д.\n")

print(f"Сортировка по цвету:\n {[(flower.color, flower.name) for flower in bouquet.sorted_by_color()]}\n")

print(f"Сортировка по цене:\n "
      f"{[(flower.price, flower.name, flower.color) for flower in bouquet.sorted_by_price()]}\n")

print(f"Поиск по цвету Белый: \n "
      f"{[(flower.name, flower.color) for flower in bouquet.search_by('color', 'Белый')]}\n")

print(f"Поиск по цене 50: \n "
      f"{[(flower.name, flower.color) for flower in bouquet.search_by('price', 50)]}\n")
