#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    return even_numbers

def make_exclamation(sentence_list):
    exclamation = [sentence + "!" for sentence in sentence_list]
    return exclamation