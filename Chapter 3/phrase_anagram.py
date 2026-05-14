"""building an anagram phrase from my name """

from itertools import permutations
import load_dictionary

dict_file = load_dictionary.load('dictionary.txt')
dict_file = [word.lower() for word in dict_file]

def make_anagrams(word):
    """making valid dictionary anagram from one word"""
    anagram = []
    for i in permutations(word):
        permu_word = ''.join(i)
        if permu_word in dict_file:
            if permu_word not in anagram:
                anagram.append(permu_word)
    return anagram

def choose_word(anagram_list):
    """user gonna choose one word"""
    print("\nChoose from these words:\n")

    for word in anagram_list:
        print(word)

    while True:
         choice = input("\nEnter your choice: ").lower()
         if choice in anagram_list:
             return choice
         
         else:
             print("Invalid choice! Enter correct choice")

def main():

    name = input("Enter your full name: ").lower()
    words = name.split()

    final_name = []

    for word in words:

        print(f"\nCurrent word = {word}")

        anagram_list = make_anagrams(word)

        if len(anagram_list) == 0:
            print("No anagrams found!")
            final_name.append(word)

        else:
            choosed_word = choose_word(anagram_list)
            final_name.append(choosed_word)
            
    print("\nFinal anagram name:\n")
    print(' '.join(final_name))


if __name__ == '__main__':
    main()
