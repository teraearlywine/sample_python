"""
PALINDROME is a word that's spelled the same forwards and backwards (racecar).
You can write an algorithm that checks if a word is a palindrome by reversing 
all the letters and testing if the reversed and original word are the same. 
"""

def palindrome(word):

    word = word.lower()
    return word[::-1] == word

print(palindrome('racecar'))
