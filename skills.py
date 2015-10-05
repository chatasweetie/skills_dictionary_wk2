# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    unique_count_list = {}
    words = input_string.split()
    for word in words:
        if word not in unique_count_list:
            unique_count_list[word] = 1
        else:
            unique_count_list[word] += 1


    return unique_count_list


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    common_words = []
    ##setting up which list is longer and shorter

    ## I struggled to make this work with a dictionary, I spent about 
    # 3 hours trying to figure it out
    if list1 > list2:
        shorter_list = list2
        longer_list = list1
    else:
        shorter_list = list1
        longer_list = list2

    for i in range(len(shorter_list)):
        for j in range(len(longer_list)):
            if shorter_list[i] == longer_list[j]:
                common_words.append(shorter_list[i])

    return common_words


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    list_set1 = set([])
    list_set2 = set([])
    for item in list1:
        list_set1.add(item)
    for item in list2:
        list_set2.add(item)
    unique_common_words = list_set1 & list_set2

    return unique_common_words


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    sum_zero_pairs = {}

    for i in range(len(input_list)): # going through the list
        for j in range(len(input_list)): # going through the list to compare
            if input_list[i] + input_list[j] == 0: #compares # to all numbers
                # print "the numbers that add up to zero for i:", input_list[i]
                # print "the numbers that add up to zero for i:", input_list[j]
                if (input_list[i], input_list[j]) not in sum_zero_pairs:
                    num = input_list[i]
                    num2 = input_list[j]                
                    key = sorted([num, num2])
                    sum_zero_pairs[tuple(key)] = 0 #I had a hard time trying to get this
                    # part for some reason, my brain didn't know how to get from my nested
                    # for loop to putting into the dictionary
    return sort_pairs(sum_zero_pairs.keys())

def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """
    removed_duplicates = []
    for word in words:
        if word not in removed_duplicates:
            removed_duplicates.append(word)

    return removed_duplicates


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
    encoded_phrase = ""

    encode_dictionary = {"e" : "p", 
                        "a" : "d",
                        "t" : "o",
                        "i" : "u" }
    for char in phrase:
        if char in encode_dictionary:
            char = encode_dictionary[char]
            encoded_phrase += char
        else:
            encoded_phrase += char

    return encoded_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    # sorted_words_length_list = []
    # for word in words:
    #     if (len(word)) not in sorted_words_length_list:
    #         sorted_words_length_list = [((len(word)), [word])]
    #         print "word:",word
    #     else:
    #         print "else word:",word
    #         sorted_words_length_list = ((len(word)), [word])
    #         sorted_words_length_list[(len(word))] = [word]

    return []


    # if (input_list[i], input_list[j]) not in sum_zero_pairs:

def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    pirate_dictionary ={"sir" : "matey", 
                        "hotel" : "fleabag inn", 
                        "student" : "swabbie", 
                        "boy" : "matey", 
                        "madam" : "proud beauty",
                        "professor" : "foul blaggart",
                        "restaurant" : "galley",
                        "your" : "yer",
                        "excuse" : "arr",
                        "students" : "swabbies",
                        "are" : "be",
                        "lawyer" : "foul blaggart",
                        "the" : "th'",
                        "restroom" : "head",
                        "my" : "me",
                        "hello" :  "avast",
                        "is" : "be",
                        "man" : "matey"}
    pirate_talk = ""

    word_list = phrase.split()

    for word in word_list:
        if pirate_talk != "":
            pirate_talk += " "
        if word in pirate_dictionary:
            new_word = pirate_dictionary[word]
            pirate_talk += new_word
        else:
            pirate_talk += word
    return pirate_talk




# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    return ''


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
