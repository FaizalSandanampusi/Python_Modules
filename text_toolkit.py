import os
import re
from collections import Counter
from itertools import islice

def word_frequency(text_or_path, filter_func=None):
    """
    Count how frequently each word appears in the text.
    Can accept a string or a file path to a text file.
    Optionally accepts a filter function to filter words.
    """
    words = _get_words(text_or_path)
    freq = Counter(words)
    
    if filter_func:
        return Counter({word: count for word, count in freq.items() if filter_func(word)})
    return freq

def unique_words(text_or_path):
    """
    Extract unique words from the text.
    """
    words = _get_words(text_or_path)
    return set(words)

def word_cooccurrence_matrix(text_or_path, window=2):
    """
    Create a word co-occurrence matrix with a given window size.
    """
    words = _get_words(text_or_path)
    cooccurrence_matrix = {}
    
    # Iterate over the words
    for i in range(len(words)):
        # Iterate over words within the window size after the current word
        for j in range(1, window):
            if i + j < len(words):
                word1 = words[i]
                word2 = words[i + j]
                pair = (word1, word2)
                cooccurrence_matrix[pair] = cooccurrence_matrix.get(pair, 0) + 1
    
    return cooccurrence_matrix

def text_generator(text_or_path):
    """
    A generator that yields one line of text at a time.
    Can accept a string of text or a file path.
    """
    if isinstance(text_or_path, str):
        if os.path.exists(text_or_path):
            # It's a file path
            with open(text_or_path, 'r') as file:
                for line in file:
                    yield line.strip()
        else:
            # It's a string of text
            if '\n' in text_or_path:
                for line in text_or_path.split('\n'):
                    yield line.strip()
            else:
                yield text_or_path.strip()
    else:
        raise ValueError("Input must be a string (text or file path)")

def _get_words(text_or_path):
    """
    Helper function to get words from either a string or a file path.
    """
    if isinstance(text_or_path, str) and '\n' not in text_or_path:
        with open(text_or_path, 'r') as file:
            text = file.read()
    else:
        text = ' '.join(text_generator(text_or_path))
    
    return re.findall(r'\b\w+\b', text.lower())

# Additional utility functions

def process_large_file(file_path, chunk_size=1000):
    """
    Process a large file in chunks using a generator.
    """
    with open(file_path, 'r') as file:
        while True:
            chunk = list(islice(file, chunk_size))
            if not chunk:
                break
            yield ''.join(chunk)

def apply_to_large_file(file_path, func, chunk_size=1000):
    """
    Apply a function to a large file in chunks.
    """
    results = []
    for chunk in process_large_file(file_path, chunk_size):
        results.append(func(chunk))
    return results