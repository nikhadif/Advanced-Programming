
def make_word_list(a_file):
    """Create a list of words from the file"""
    word_list = []

    
    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            if 