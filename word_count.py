# word_count.py

import string
from collections import Counter

FILE_NAME = "sample.txt"

def clean_text(text):
    """Lowercase and remove punctuation."""
    translator = str.maketrans("", "", string.punctuation)
    return text.lower().translate(translator)

def main():
    try:
        with open(FILE_NAME, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: {FILE_NAME} not found!")
        return

    cleaned = clean_text(text)
    words = cleaned.split()
    word_counts = Counter(words)

    print("10 most common words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
