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

def character_count():
    characters_counted = {}
    # Grab frankenstein.txt with path and call it frankenstein
    with open("/home/johaleia/workspace/github.com/Alex-Hardin/bookbot/books/frankenstein.txt", "r") as frankenstein:
        content = frankenstein.read()
        # You cant .lower() a txt file so we used content = frankenstein.read() to get around that
        frank_lower = content.lower()
        for word in frank_lower:
            for char in word:
                if char in characters_counted:
                    characters_counted[char] += 1
                else:
                    characters_counted[char] = 1
    print(characters_counted)

character_count()


