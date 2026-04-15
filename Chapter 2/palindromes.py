"""finding palindromes in a dictionary file."""

import load_dictionary

word_list = load_dictionary.load("dictionary.txt")

palindromes_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindromes_list.append(word)

print("\nNumbers of the palindromes in the dictionary: {}\n".format(len(palindromes_list)))
print("The palindromes in the dictionary are: \n")
for palindrome in palindromes_list:
    print(palindrome, sep="\n")
