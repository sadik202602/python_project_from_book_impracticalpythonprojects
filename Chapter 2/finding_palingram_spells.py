"""Finding all word_pair that are palingram in a dictionary file."""

import Load_dictionary
import time

word_list = Load_dictionary.load("dictionary.txt")

def find_palingrams():
    """finding palingrams in a dictionary file."""
    palingrams_list = []

    words = set(word_list)

    for word in words:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):
                #1st - last part the is a palindrome and first part is in the dictionary
                if word[i:] == rev_word[:end-1] \
                      and rev_word[end-1:] in words:
                    palingrams_list.append((word, rev_word[end-1:]))
                #2nd - first part the is a palindrome and last part is in the dictionary
                if word[:i] == rev_word[end-i:] \
                        and rev_word[:end-i] in words:
                    palingrams_list.append((rev_word[:end-i], word))
    return palingrams_list

start_time = time.time()
#calling the function and print the result
palingrams = find_palingrams()
end_time = time.time()

print("\nTime to find palingrams: {:.2f} seconds\n".format(end_time - start_time))

palingrams_sorted = sorted(palingrams)
print("\nNumbers of the palingrams in the dictionary: {}\n".format(len(palingrams_sorted)))

for first, second in palingrams_sorted:

    print("{} {}".format(first, second))
