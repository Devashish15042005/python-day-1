def contain_vowel(s):
    vowels = "AEIOUaeiou"
    for char in s:
        if char in vowels:
            return True 
    return False
print(contain_vowel("devashish"))
