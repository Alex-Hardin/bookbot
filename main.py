def main():
    with open("/home/johaleia/workspace/github.com/Alex-Hardin/bookbot/books/frankenstein.txt") as f:
        read_contents = f.read()
        print(read_contents)

def word_count():
    # Grab frankenstein.txt with path and call it frankenstein
    with open("/home/johaleia/workspace/github.com/Alex-Hardin/bookbot/books/frankenstein.txt") as frankenstein:
        # Word counter
        words = 0
        # Loop through each word in frankenstein
        for word in frankenstein:
            # Word.split() splits each line into a list of words based on whitespace
            words_split = word.split()
            # Add the number of words to the counter above.
            words += len(words_split)
    print(words)

word_count()