marks ={
    "bishesh" :100,
    "ankit" : 20,
    "aashish": 5,
}
print(marks.items())    #.items methods
print(marks.keys())      #.keys methos
print(marks.values())      #.values method
marks.update({"bishesh": 99, "renuka": 50})
print(marks) #update method

print(marks.get("bishesh")) #prints none and returns an error
print(marks["bishesh"])