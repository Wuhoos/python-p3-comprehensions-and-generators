#!/usr/bin/env python3

def return_evens(num_list):
    return [ n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    else:
        return [sentence + "!" for sentence in sentence_list]