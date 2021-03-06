"""
Set of functions that process texts.
They are meant as parameters of GraphBuilder objects
"""
import string
import enchant

import nltk


def clean_stopwords(tokens):
    """
    Removes stopwords from a list of words
    """
    stopwords = nltk.corpus.stopwords.words('english')
    not_stop_words = []
    for token in tokens:

        if not token in stopwords:
            not_stop_words.append(token)

    return not_stop_words

def remove_punctuation(tokens):
    """
    Removes punctuation from a list of tokens
    It uses string.punctuation list of punctuation
    """
    REMOVE_PUNCTUATION_MAPPING = dict.fromkeys(map(ord, string.punctuation))

    not_punct_words = []
    for token in tokens:

        # Careful: not enough for unicode punctuation, ie. spanish or other languages
        # punctuation symbols. Not important in this context though.
        not_punct_token = token.translate(REMOVE_PUNCTUATION_MAPPING)
        if not not_punct_token == '':
            not_punct_words.append(not_punct_token)

    return not_punct_words

def remove_dictionary_words(tokens):
    """
    Removes words present in the dictionary
    """
    d = enchant.Dict("en_US")
    new_tokens = []
    for token in tokens:
        if not d.check(token):
            new_tokens.append(token)
    return new_tokens

def clean_punctuation_and_stopwords(tokens):
    tokens = remove_punctuation(tokens)
    tokens = clean_stopwords(tokens)
    return tokens

def only_non_dictionary_words(tokens, remove = ['nt', 've', 'fox', 'huff', 'cnn']):
    tokens = remove_punctuation(tokens)
    tokens = clean_stopwords(tokens)
    tokens = remove_dictionary_words(tokens)
    # To do: some particles like nt remain...

    def _passes(word):
        if sum(p in word for p in remove) > 0:
            return False
        return word.isalpha()
        # return True

    return [t for t in tokens if _passes(t)]


