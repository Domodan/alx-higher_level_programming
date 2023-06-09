#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    return l, sentence[0] if sentence else None
