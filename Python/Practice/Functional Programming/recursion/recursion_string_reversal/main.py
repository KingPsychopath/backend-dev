def reverse_string2(s):
    if len(s) == 0:
        return s
    next_character = reverse_string(s[1:]) + s[0]
    return next_character

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]