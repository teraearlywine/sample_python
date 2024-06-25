""" 
Anagram is a word created by rearranging letters of another word. 
Sorted arranges the characters in each word alphabetically. 
The anagram function then tests if they're the same
"""

def anagram(word1, word2): 
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2) 


print(anagram("iceman", "cinema"))