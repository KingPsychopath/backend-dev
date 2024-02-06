def remove_invalid_lines(document):
    return '\n'.join(list(filter(lambda x:  '-' not in x, document.split('\n'))))

# Solution Version
def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )
