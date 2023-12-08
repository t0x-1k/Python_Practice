def break_words(stuff):
    #This functionwill break up words for us.
    words = stuff.split(' ')
    return words

def sort_words(words):
    #This will sort the words
    return sorted(words)

def print_first_word(words):
    #this will print out the first word in our list
    word = words.pop(0)
    print(word)

def print_last_word(words):
    #this will print out the last word in our list
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    #this will take a full sentence and sort it by the letters in each word
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
