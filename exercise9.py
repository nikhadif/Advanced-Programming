
def are_anagrams(word1, word2):
     """Return True, if words are anagrams."""
     word1_sorted = sorted(word1)
     word2_sorted = sorted(word2)

     return word1_sorted == word2_sorted

print("Anagram Test")


two_words = input("Enter two space separated words: ")
word1,word2 = two_words.split()

if are_anagrams(word1, word2):
   print("The words are anagrams.")
else:
   print("The words are not anagrams.")
