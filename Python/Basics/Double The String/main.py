def double_string(string):
    new_word = []

    for i in string:
        new_word.append(i)
        new_word.append(i)

    sentence = ''.join(new_word)
    print(sentence)
    return sentence

def double_string2(string):
    output = ""
    for i in string:
        output = output + i * 2
    return output