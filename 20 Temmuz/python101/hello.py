sozluk = {"elma":"apple", "muz":"banana", "uzum":"grapes", "havuc":"carrot",}

reversed_sozluk = {}
for i , j in sozluk.items():
     reversed_sozluk[j] = reversed_sozluk.get(j , [])
     reversed_sozluk[j].append(i)

 

