def get_last_n_items(items, n):
    # Səhv: Slicing (dilimləmə) indeksi səhvdir
    return items[len(items) - n + 1:]

my_list = [10, 20, 30, 40, 50]
print(get_last_n_items(my_list, 3)) # Gözlənilən: [30, 40, 50]
