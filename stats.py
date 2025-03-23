def get_num_words(text):
    string = text.split()
    num_words = len(string)
    return num_words

def count_characters(text):
    text = text.lower()
    characters_count = {}
    
    for i in text:
        if i not in characters_count:
            characters_count[i] = 1
        else:
            characters_count[i] = characters_count[i] + 1
    
    return characters_count