# -*- coding: utf-8 -*

from itertools import permutations
import load_dictionary


# dictionary file load করছি
dict_file = load_dictionary.load('dictionary.txt')

# সব word lowercase করছি
dict_file = [word.lower() for word in dict_file]


def make_anagrams(word):
    """Make valid dictionary anagrams from one word."""

    anagrams = []

    # permutations বানাচ্ছে
    for i in permutations(word):

        # tuple → string
        perm_word = ''.join(i)

        # যদি dictionary তে থাকে
        if perm_word in dict_file:

            # duplicate যেন না আসে
            if perm_word not in anagrams:
                anagrams.append(perm_word)

    return anagrams


def choose_word(anagram_list):
    """Let user choose one word."""

    print("\nChoose from these words:\n")

    # সব possible words দেখাও
    for word in anagram_list:
        print(word)

    while True:

        choice = input("\nEnter your choice: ").lower()

        # choice valid কিনা check
        if choice in anagram_list:
            return choice

        else:
            print("Invalid choice! Try again.")


def main():

    # full name input
    name = input("Enter your full name: ").lower()

    # name split করছি
    words = name.split()

    # final chosen words এখানে জমা হবে
    final_name = []

    # প্রতিটা word এর জন্য loop
    for word in words:

        print(f"\nCurrent word = {word}")

        # valid anagrams বের করছি
        anagram_list = make_anagrams(word)

        # যদি কিছু না পাওয়া যায়
        if len(anagram_list) == 0:
            print("No anagrams found!")
            final_name.append(word)

        else:
            # user choose করবে
            chosen_word = choose_word(anagram_list)

            # final list এ save করছি
            final_name.append(chosen_word)

    print("\nFinal anagram name:\n")

    # list কে sentence বানাচ্ছে
    print(' '.join(final_name))


if __name__ == '__main__':
    main()
