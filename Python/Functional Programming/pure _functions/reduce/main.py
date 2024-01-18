import functools


def accumulate(doc, sentence):
    if not doc or doc == "":
        return sentence
    return doc + ". " + sentence


def accumulate_first_sentences(sentences, n):
    if not sentences:
        return ""
    if len(sentences) <= n:
        return functools.reduce(accumulate, sentences) + "."
    return functools.reduce(accumulate, sentences[:n]) + "."
