def markdown_to_text(doc_content):
    lines = doc_content.split("\n")

    new_lines = []
    for line in lines:
        if line.startswith("#"):
            line = line[1:].strip()
        new_line = remove_asterisks_from_words(line)
        new_lines.append(new_line)

    return "\n".join(new_lines)


def remove_asterisks_from_words(line):
    words = line.split()
    for i, word in enumerate(words):
        if word.startswith("*"):
            word = word[1:]
        if word.endswith("*"):
            word = word[:-1]
        if len(word) == 0:
            continue
        words[i] = word
    return " ".join(words)