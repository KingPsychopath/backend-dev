def remove_asterisks_from_word(word):
    if len(word) == 1:
        return word
    if word.startswith('*'):
        word = word[1:]
    if word.endswith('*'):
        word = word[:-1]
    return word

def remove_asterisks_from_line(line):
    words = line.split(' ')
    words = list(map(remove_asterisks_from_word, words))
    print('Test 2.5:', words)
    return ' '.join(words)

def remove_hash_at_start(line):
    header_character = "#"
    if len(line) > 0 and line[0] == header_character:
        return "" + line[2:] # Start at index 2 because we are skipping the hash and the space after it
    return line

def markdown_to_text(doc_content):
    lines = doc_content.split('\n')
    print('          Test1', lines)
    
    lines = (list(map(remove_hash_at_start, lines)))

    print('          Test2', lines)

    lines = (list(map(remove_asterisks_from_line, lines)))

    print('          Test3', lines)

    return '\n'.join(lines)