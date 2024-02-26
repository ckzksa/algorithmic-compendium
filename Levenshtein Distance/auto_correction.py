import re

from levenshtein_distance import *

def load_dictionary(file_path):
    with open(file_path, 'r') as f:
        words = f.readlines()
    return set(word.strip().lower() for word in words)

def get_correction(words, dictionary, limit=None):
    if len(dictionary) <= 0:
        return None
    
    if not limit:
        limit = len(dictionary)
    
    best_corrections = {}
    for word in words:
        if word not in dictionary:
            corrections = sorted(((item, levenshtein_distance(word, item)) for item in dictionary), key=lambda x: x[1])
            
            best_corrections[word] = []
            for correction, value in corrections:
                if value != corrections[0][1]:
                    break
                best_corrections[word].append(correction)
                
    return best_corrections

def auto_correct(text, dictionary):
    words = re.findall(r'\b\w+\b', text.lower())
    corrections = get_correction(words, dictionary, limit=None)
    corrected_text = text
    
    for word, corrections in corrections.items():
        corrected_text = re.sub(r'\b' + word + r'\b', corrections[0], corrected_text, flags=re.IGNORECASE)
    
    return corrected_text
    
if __name__ == "__main__":
    dictionary = load_dictionary("dictionary.txt")
    corrections = get_correction(["vat", "beer"], dictionary)
    print(corrections)
    print()
    
    text = "ths is am examplle"
    print(f"Misspelled text: {text}")
    text = auto_correct(text, dictionary)
    print(f"Text correctly spelled: {text}")