import random 
print(random.randint(1,6))

friend = ["aman","ayan","dev","aradhya","tanya"]
print(random.choice(friend))

num = list(range(1,11))
random.shuffle(num)
print(num)