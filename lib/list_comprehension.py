#!/usr/bin/env python3

def return_evens(num_list):
    return [num_list[n] for n in range(len(num_list)) if num_list[n]%2 == 0]


def make_exclamation(sentence_list):
    return [sentence_list[n]+"!" for n in range(len(sentence_list)) if len(sentence_list) != 0]