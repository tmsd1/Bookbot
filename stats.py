from ast import List


def get_num_words(text):
    s = 0
    for i in text.split():
        s+=1
    return s


def count_characters(text):
        c = {}
        for i in text:
            c[i.lower()] = c.get(i.lower(), 0) + 1
        return c


def sort_on(l):
   orders = list(l.items())
   orders.sort(key=lambda x:x[1], reverse=True)
   for i in orders:
    print(f"{i[0]}: {i[1]}")
   return orders

    