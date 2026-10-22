#Write a function count_vowels(text) that counts the vowels (a, e, i, o, u) in a string.

def count_vowels(text):
    count = 0
    vowels = ["a","e","i","o","u"]
    for i in text:
        if i in vowels :
            count+=1
    print(f"the total vowels in text {count} ")
    return count

count_vowels("heeeeeoooiillo")        

