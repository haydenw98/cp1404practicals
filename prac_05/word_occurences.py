"""
Word Occurrences
Estimate: 30 minutes
Actual: 14 minutes
"""


def main():
    """Counts the occurrences of a word in user inputted text and prints"""
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
    width = max(len(word) for word in words)
    for word in words:
        print(f"{word:{width}} : {word_to_count[word]}")
main()
