"""Find all single word anagrams for a given word using a dictionary file."""

import load_dictionary

words_list = load_dictionary.load('dictionary.txt')

anagram_lists = []

name = input("Enter a name to find anagrams for: ")
print(f"input name = {name}")

name = name.lower()
print(f"Using name = {name}")

name_sorted = sorted(name)

for word in words_list:
    word = word.lower()
    if not word == name:
        if sorted(word) == name_sorted:
            anagram_lists.append(word)

print("You need a larger dictionary or a new name!" if len(anagram_lists) == 0
      else f"Anagrams of {name}: {', '.join(anagram_lists)}")

