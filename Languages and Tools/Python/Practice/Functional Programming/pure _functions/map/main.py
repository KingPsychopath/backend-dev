
# Not functional too much how, just enough what should be done - but it works
def change_bullet_style2(document):
    # Split the Document By newLine character, creating an array where each index is an element with each line
    lines = document.split('\n')
    print(lines)
    new_document = map(convert_line, lines)
    new_document = '\n'.join(new_document)
    return new_document

# This is the functional way
def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split("\n")))


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
