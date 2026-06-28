#create a ampty dictionarya and allow4 friend to enter their favourite language  as values and use key as their names.assume thst the names are unique
d={}
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name:lang})
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name:lang})
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name:lang})
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name:lang})
print(d)