# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word = sorted(word)
    anagram = sorted(anagram)
    
    if word == anagram:
        return True
    else:
        return False
        
