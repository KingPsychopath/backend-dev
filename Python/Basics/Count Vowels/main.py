def count_vowels(text):
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for char in text:
        if char.lower() in vowels:
            vowels[char.lower()] += 1

    print(vowels)
    sum = 0
    for vowel_count in vowels:
        sum += vowels[vowel_count]

    return sum

    
def count_vowels2(text):
    count = 0
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    for char in text:
        if char in vowels:
            count += 1
    return count