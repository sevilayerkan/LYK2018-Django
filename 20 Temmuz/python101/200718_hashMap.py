#lyk2018 Django: 20.07.18 - 21.07.18

sozluk = {"elma": "apple", "muz": "banana", "uzum": "grapes", "havuc": "carrot", }
reversed_sozluk = {}

#Reversed dictionary icin kisisel cozumum
for i , j in sozluk.items():
     reversed_sozluk[j] = reversed_sozluk.get(j , [])
     reversed_sozluk[j].append(i)
 
print(sozluk)
print(reversed_sozluk)

#StackOverflow : inv_map = {v: k for k, v in sozluk.items()} #pytonic way

#Simple way
inv_map = {}
for a,b in sozluk.items():
     inv_map[b] = a

print(inv_map)

# todo : tekrar dene
# inv_map.update('apple' = 'portakal')
# print("Updated dict : ")
# print(inv_map)

fatih = {
     "lyk" : "2018",
     "gorev" : "hoca",
     "key" : "fatih",
     "sinif" : "201"
}

tunahan ={
     "lyk": "2018",
     "gorev": "ogrenci",
     "key": "fatih",
}
print()
print(fatih)
print(tunahan)
print()

# Pythonic" way
# d = {a:i for i,a in fatih.items()}

# list comprehension
# [key for key,value in fatih.items()]
# [(key,value) for key,value in fatih.items()]
# [(value.key) for key,value in fatih.items()]


reverseDic_pythonic = dict([(value,key) for key,value in fatih.items()])
print(reverseDic_pythonic)



