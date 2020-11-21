
def are_anagrams(word1, word2):
     """Return True, if words are anagrams."""
     word1_sorted = sorted(word1)
     word2_sorted = sorted(word2)

     return word1_sorted == word2_sorted

print("Anagram Test")


valid_input_bool = False
while not valid_input_bool:
    try:
        two_words = input("Enter two spaces separated words: ")
        word1,word2 = two_words.split()

        valid_input_bool = True
    except ValueError:
        print("Bad Input")

if are_anagrams(word1, word2):
    print("The words {} and {} are anagrams.".format(word1, word2))
else:
    print("The words {} and {} are not anagrams.".format(word1, word2))
