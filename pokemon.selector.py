import random
respond = ("yes","no")
pokemon = ("pikachu","chaarizard","blastoise","bayleaf","torors")

pokemon = random.choice(pokemon)
print("enter to get a pokemon")
respond = input("enter a choice:")
if respond =="yes":

 print(pokemon)
else:
 print("i think you like other shows more")