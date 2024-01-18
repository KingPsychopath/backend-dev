valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    zipped = list(zip(doc_names, doc_formats))
    return filter(lambda x: x[1] in valid_formats, zipped)