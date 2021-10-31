parameters_levels = ['Белый соус', 'Карамельный сироп', 'Кленовый сироп', 'Клубничный сироп', 'Черничный сироп', 'Молочный шоколад']
#parameters_levels = [(parameters_levels[i:i + 3] for i in range(0, len(parameters_levels), 3))]
def func(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#print(list(func(parameters_levels,3)))

parameters_levels1 = [parameters_levels[i:i + 3] for i in range(0, len(parameters_levels),3)]
#print(parameters_levels)
#print(list(parameters_levels1))

def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs
buttons_list = split(parameters_levels, 3)
buttons_list.append(['ГЛАВНОЕ МЕНЮ'])
print(buttons_list)