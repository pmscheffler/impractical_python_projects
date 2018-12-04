"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

filename = input('Please enter the filename to load: ')
word_list = load_dictionary.load(filename)

def remove_single_letters(all_words):
    """ Parse a list of words and remove any that are a single letter except the permissible ones """

    permissible = ('a','i')

    # remove words in the passed in list
    for word in all_words:
        if len(word) == 1 and word not in permissible:
            all_words.remove(word)

    return all_words

# find word-pair paligrams
def find_palingrams():
    """Find dictionary paligrams."""
    pali_list = []
    words = set(remove_single_letters(word_list))

    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i]and rev_word[end-i:]in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:]and rev_word[:end-i]in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of paligrams
print('\nNumber of palingrams = {}\n'.format(len(palingrams_sorted)))

input('Press any key to see the list of palingrams')

for first, second in palingrams_sorted:
    print("{} {}".format(first, second))


