
def main():
        with open("/home/johaleia/workspace/github.com/Alex-Hardin/bookbot/books/frankenstein.txt") as franken: 
            read_contents = franken.read()
        return(read_contents)

def word_count():
    # changed to use main function to pull txt file ***Don't Repeat Yourself****
    franken_read = main()
    words_split = franken_read.split()
    return len(words_split)

def character_count():
    # changed to use main function to pull txt file ***Don't Repeat Yourself****
    franken_read = main()
    characters_counted = {}
    # changed to convert franken_read to return lowercases before loop
    franken_read = franken_read.lower()
    # loop each word in frankenstein.txt
    for word in franken_read:
        # loop each character in letter
        for char in word:
            # if char is already in characters_counted list then += 1
            if char in characters_counted:
                characters_counted[char] += 1
            else:
                # if char NOT in characters_counted list then char = 1
                characters_counted[char] = 1
    # Had to AI this for help. Will come back to update in a form that makes more sense to me at a later date. 
    letters_only = {char: count for char, count in characters_counted.items() if ('a' <= char <= 'z')}
    # making dictionary into list so I can sort
    letters_list = [{"char": char, "count": count} for char, count in letters_only.items()]
    # sort with reverse=TRUE so top number is the large number. key = dict_sort which is my function below returning the num value
    letters_list.sort(reverse=True, key=dict_sort)
    return letters_list

def dict_sort(dict):
    return dict["count"]

def print_report():
    # pull in character_count function
    new_list = character_count()
    print(f"--- Begin report of books/frankenstein.txt --- \n{word_count()} words found in the document")
    for item in new_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")

print_report()
