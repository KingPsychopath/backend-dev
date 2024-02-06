def categorize_file(filename):
    # ?
    file_type = {
        '.txt': 'Text',
        '.docx': 'Document',
        '.py': 'Code'
    }
    get_category = lambda x: file_type.get(x, 'Unknown')
    return get_category(filename[filename.rfind(".") :])