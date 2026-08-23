word = input("enter any word").lower()
vowel = ['a','e','i','o','u']
count = 0
for ch in word:
    if ch in vowel:
     count +=1
     print("vowel in word",count)
    else:
     print("no vowel")

