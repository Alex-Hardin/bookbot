"""
def main():
        with open("/home/johaleia/workspace/github.com/Alex-Hardin/bookbot/books/frankenstein.txt") as f: 
            read_contents = f.read()
        print(read_contents)
"""

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
    return(words)

def character_count():
    characters_counted = {}
    # Grab frankenstein.txt with path and call it frankenstein
    with open("/home/johaleia/workspace/github.com/Alex-Hardin/bookbot/books/frankenstein.txt", "r") as frankenstein:
        content = frankenstein.read()
        # You cant .lower() a txt file so I used content = frankenstein.read() to get around that
        frank_lower = content.lower()
        for word in frank_lower:
            for char in word:
                if char in characters_counted:
                    characters_counted[char] += 1
                else:
                    characters_counted[char] = 1
    letters_only = {char: count for char, count in characters_counted.items() if ('a' <= char <= 'z')}
    letters_list = [{"char": char, "num": count} for char, count in letters_only.items()]
    letters_list.sort(reverse=True, key=dict_sort)
    return letters_list
   
   

def dict_sort(dict):
    return dict["num"]


def print_report():
    new_list = character_count()
    print(f"--- Begin report of books/frankenstein.txt --- \n{word_count()} words found in the document")
    for item in new_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

print_report()