
"""write a script that will ask for a string and tell 
if a letter in the string is a vowel or consonant
"""
my_string=input("please enter a word:  ").strip()
num_c=0
num_v=0

for i in my_string:
    if i in 'aeiou':
        num_v+=1
    else:
       num_c+=1  # type: ignore
print(f"number of vowel is: {num_v}")       
print(f"number of consonant is: {num_c}")       