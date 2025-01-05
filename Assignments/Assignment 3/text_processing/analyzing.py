# function: count word frequency
def count_word_frequency(text):
    word_frequency = {}
    words = text.split()

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
            
    return word_frequency


