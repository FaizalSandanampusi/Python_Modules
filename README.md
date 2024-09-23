# Text Toolkit

The `text_toolkit` module provides a set of utilities for processing and analyzing text data. It allows users to compute word frequencies, extract unique words, generate co-occurrence matrices, and handle large text files efficiently. This toolkit is useful for text analysis, natural language processing, and data preparation tasks.

## Functions and Usage

### word_frequency

The `word_frequency` function counts how frequently each word appears in the provided text. It can accept either a string of text or a path to a text file. Additionally, you can pass an optional filter function to filter the words based on specific criteria.

```python
import text_toolkit as tt

freq = tt.word_frequency('example.txt')
print(freq)
```

### unique_words

The `unique_words` function extracts and returns the unique words from the text. This is helpful for understanding the vocabulary used in a document.

```python
unique = tt.unique_words('example.txt')
print(unique)
```
### _get_words

The `_get_words` function is a helper function that retrieves words from either a string or a file path. It reads the content and extracts words, returning them in lowercase.

```python
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
```

### word_cooccurrence_matrix

The `word_cooccurrence_matrix` function creates a matrix that captures how often pairs of words occur together within a specified window size. This can be useful for analyzing relationships between words.

```python
cooccurrence_matrix = tt.word_cooccurrence_matrix('example.txt', window=2)
print(cooccurrence_matrix)
```

### text_generator

The `text_generator` function is a generator that yields one line of text at a time. It can handle both strings of text and file paths, making it versatile for processing large documents.

```python
for line in tt.text_generator('example.txt'):
    print(line)
```

### process_large_file

The `process_large_file` function allows you to process a large text file in chunks, using a generator to yield segments of the file. This is particularly useful for memory-efficient handling of very large files.

```python
for chunk in tt.process_large_file('large_file.txt', chunk_size=1000):
    print(chunk)
```

### apply_to_large_file

The `apply_to_large_file` function applies a specified function to a large text file in chunks. This is useful for processing large datasets where you want to perform operations on smaller sections of the file.

```python
results = tt.apply_to_large_file('large_file.txt', some_function, chunk_size=1000)
print(results)
```

### Test

The test file is `session14_test.py`. The test file contains test cases for all the functions in the `text_toolkit` module.

The tests have passed locally and below is the screenshot of the tests passing in terminal.

![alt text](image.png)



## Conclusion

The `text_toolkit` module is designed to simplify text processing tasks, making it easier to analyze and manipulate text data. With its functions, users can efficiently count word frequencies, find unique words, generate co-occurrence matrices, and handle large files without overwhelming system resources.
