"""
Word Occurrences
Estimate: 30 minutes
Actual: 14 minutes
"""


def main():
    """Count the occurrences of a word in user inputted text and prints."""
    word_to_count = {}
    text = input("Text: ")
    words = text.split()
    for word in words:
        word = word.lower()
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    words = sorted(word_to_count.keys())
    max_word_length = max(len(word) for word in words)
    for word in words:
        print(f"{word:{max_word_length}} : {word_to_count[word]}")
main()
