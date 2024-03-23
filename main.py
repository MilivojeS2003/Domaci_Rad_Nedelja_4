# 1. Data je lista stringova ["flower","flow","flight"]. Napisati funkciju koja koristi reduce da nađe najduži
# string među datim stringovima.

from functools import reduce
# my_list = ["flowerr","flow","flight"]
#
# print(reduce(lambda x,y: x if(len(x) > len(y)) else y, my_list))



# 2. Date su dvije liste, jedna sa imenima studenata, a druga sa njihovim prosječnim ocjenama.
# Napisati funkciju koja pronalazi studente sa prosječnom ocjenom iznad 8.5 i vraća listu torki (ime,
# ocjena) za te studente.

# def indeks_korisnik(lista,lista2):
#     niz = []
#     for item in range(len(lista)):
#         if lista[item] >= 8.5:
#             niz.append(lista2[item])
#     return niz
# ime_studenata = ["Milivoje" , "Nikola" , "Petar" , "Uros"]
# prosjek_studenata = [10, 8.9, 8.0, 7.9]
#
# print(indeks_korisnik(prosjek_studenata,ime_studenata))


# 3. Data je lista rječnika oblika [{ 'ime': 'Ana', 'godine': 22, 'prosek': 9.1 }, ...]. Napisati funkciju koja
# filtrira studente starije od 21 godine i sortira ih po prosjeku, koristeći filter, sort i lambda funkcije.

# studenti = [
#     {'ime': 'Ana', 'godine': 22, 'prosek': 9.1},
#     {'ime': 'Marko', 'godine': 25, 'prosek': 8.5},
#     {'ime': 'Maja', 'godine': 21, 'prosek': 9.3},
#     {'ime': 'Ivan', 'godine': 23, 'prosek': 8.9}
# ]
#
# studenti_godine = filter(lambda x: x['godine'] > 21,studenti)
# studenti_godine = sorted(studenti_godine,key = lambda x:x['prosek'])
# print(list(studenti_godine))


# 4. Data je lista ["Hello, World!", "Python is cool", "Functional programming rocks"]. Napisati funkciju
# koja broji ukupan broj riječi u svim stringovima koristeći map i reduce.
# rijeci = ["Hello, World!", "Python is cool", "Functional programming rocks"]
# lista = []
# def broj_razmaka(str):
#     broj_razmaka = 1
#     for item in str:
#         if item == " ":
#             broj_razmaka += 1
#     return broj_razmaka
#
# lista = map(broj_razmaka , rijeci)
# print(reduce(lambda x,y: x+y , lista))


# 5. Data je lista torki oblika [(ime, ocjena, predmet), ...]. Napisati funkciju koja koristi filter, map, i
# reduce da izračuna prosječnu ocjenu po predmetu
#
# ocjene = [('Ana', 8, 'Matematika'), ('Ivan', 7, 'Fizika'), ('Maja', 9, 'Engleski'), ('Ivan', 9, 'Fizika')]
#
#
# def prosjek_ocjene(ocjene,predmet):
#
#     niz_ocjena = []
#     niz_ocjena = filter(lambda x: x[2] == predmet,ocjene)
#     niz_ocjena = map(lambda x: x[1], niz_ocjena)
#     niz_ocjena = list(niz_ocjena)
#     if len(niz_ocjena) != 0:
#         print(reduce(lambda x,y: x+y, niz_ocjena) / len(niz_ocjena))
#     else:
#         print("Nema tog pretmeta")
#
# prosjek_ocjene(ocjene, "Fizika")

# 6. Dat je niz vrijednosti koji predstavlja vremensku seriju. Napisati funkciju koja koristi map da
# izračuna promjenu (diferenciju) između svakog uzastopnog para vrednosti.
#
# temperatura = [
#     ('2024-03-01', 15),
#     ('2024-03-02', 17),
#     ('2024-03-03', 16),
#     ('2024-03-04', 18),
#     ('2024-03-05', 20),
#     ('2024-03-06', 19),
#     ('2024-03-07', 22)
# ]
# Pitanje: Kako da izbjegnem da svaki put koristim list()
# novi_niz = map(lambda temp : temp[1], temperatura)
# novi_niz = list(novi_niz)
# #pravimo niz tuple koji ima parove uzastopnih dana, tako sto jedan skracujemo za jedan od pozadi, a drugi za jedan od naprijed
# novi_niz = zip(novi_niz[:-1] , novi_niz[1:])
# novi_niz = list(novi_niz)
# niz = map(lambda x: x[1] - x[0], novi_niz)
# print(list(niz))


# 7. Data je lista ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']. Napisati funkciju koja koristi
# map i reduce da izračuna frekvenciju svakog elementa.

from functools import reduce


##fibonacijev niz

# duzina = int(input("duzina niza: "))
# niz = [0,1]
# for i in range(2,duzina):
#     niz.append(niz[i-1] + niz[i-2])
#
# print(niz)
#
# def fib(num):
#     a=0
#     b=1
#     i=0
#     for i in range(num):
#         yield b
#         temp = b
#         b = a + b
#         a = temp
#
# for i in fib(20):
#     print(i)


# file = open('my_file.txt')
# contest = file.read()
# for item in contest:
#     print(item)
# print(contest)








