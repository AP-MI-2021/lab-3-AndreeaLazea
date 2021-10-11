def printMenu():
    print("1. citire lista")
    print("2. cea mai lunga subsecventa in care suma numerelor este numar prim")
    print("3. cea mai lunga subsecventa in care numarul de cifre este in ordine descrescatoare")
    print("4. cea mai lunga subsecventa in care produsul numerelor este impar")
    print("5. iesire")

def citireLista():
    l = []
    n = int(input("dati numarul de elemente din lista: "))
    for i in range(n):
        l.append(int(input("l[ " + str(i) + " ] = ")))
    return l

def sum_is_prime(l):
    '''
    verifica daca suma elementelor din lista este un numar prim
    :param l: o lista de nr. intregi
    :return: True, daca suma lor este un numar prim si False in caz contrar
    '''
    sum = 0
    for x in l:
        sum = sum + x
    if sum < 2:
        return False
    else:
        for i in range(2, sum // 2 + 1):
            if sum % i == 0:
                return False
    return True

def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa a carei suma este un numar prim
    :param lst: o lista de nr. intregi
    :return: returneaza cea mai lunga subsecventa a carei suma este un numar prim
    '''
    subsecventa_maxima = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if sum_is_prime(lst[i:j + 1]) and len(subsecventa_maxima) < len(lst[i: j + 1]):
                subsecventa_maxima = lst[i:j + 1]
    return subsecventa_maxima

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([2, 1, 1, 1, 1, 1, 1, 1, 3]) == [1, 1, 1, 1, 1, 1, 1]
    assert get_longest_sum_is_prime([0, 1, 3, 1, 2, 2, 3]) == [0, 1, 3, 1, 2]
    assert get_longest_sum_is_prime([]) == []

def numarare(x: int):
    '''
    returneaza numarul de cifre
    :param x: un numar intreg
    :return: returneaza numarul de cifre
    '''
    nr = 0
    while x != 0:
        nr = nr + 1
        x = x / 10
    return nr

def numar_cifre(l):
    '''
    verifica daca numarul de cifre este in ordine descrescatoare
    :param l: o lista de numere intregi
    :return: True, daca numarul de cifre este in ordine descrescatoare si False in caz contrar
    '''
    for i in range(len(l)-1):
        if numarare(l[i]) < numarare(l[i+1]):
            return False
    return True

def get_longest_digit_count_desc(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa in care numărul de cifre este în ordine descrescătoare.
    :param lst: o lista de nr. intregi
    :return: returneaza cea mai lunga subsecventa in care numărul de cifre este în ordine descrescătoare.
    '''
    subsecventa_maxima = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if numar_cifre(lst[i:j + 1]) is True and len(subsecventa_maxima) < len(lst[i: j+1]):
                subsecventa_maxima = lst[i:j + 1]
    return subsecventa_maxima

def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([12345, 1234, 23, 1, 567, 89, 90, 0]) == [12345, 1234, 23, 1]
    assert get_longest_digit_count_desc([]) == []
    assert get_longest_digit_count_desc([4444, 444, 44, 40, 1, 12, 1234]) == [4444, 444, 44, 40, 1]

def produs_impar(l):
    '''
    determina daca produsul listei este sau nu un numar impar
    :param l: o lista de numere intregi
    :return: True, daca produsul este impar si False daca este par
    '''
    prod = 1
    for x in l:
        prod = prod * x
    if prod%2==0:
        return False
    return True

def get_longest_product_is_odd(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa a carei produs este numar impar
    :param lst: o lista de nr. intregi
    :return: returneaza cea mai lunga subsecventa a carei produs este un numar impar
    '''
    subsecventa_maxima = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if produs_impar(lst[i:j+1]) is True and len(subsecventa_maxima) < len(lst[i:j+1]):
                subsecventa_maxima = lst[i:j + 1]
    return subsecventa_maxima

def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([1, 3, 5, 0, 0, 7, 6]) == [1, 3, 5]
    assert get_longest_product_is_odd([]) == []
    assert get_longest_product_is_odd([5, 7, 10, 3, 3, 3, 3, 0, 9, 9]) == [3, 3, 3, 3]

def main():
    test_get_longest_digit_count_desc()
    test_get_longest_sum_is_prime()
    l = []
    while True:
        printMenu()
        optiune = input("dati optiunea: ")
        if optiune == '1':
            l = citireLista()
        elif optiune == '2':
            print(get_longest_sum_is_prime(l))
        elif optiune == '3':
            print(get_longest_digit_count_desc(l))
        elif optiune == '4' :
            print(get_longest_product_is_odd(l))
        elif optiune == '5':
            break
        else:
            print("optiune gresita, reincercati!")

main()
