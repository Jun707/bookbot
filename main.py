def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book(book_path)
    word_count = get_words_count(file_contents)
    char_count = words_freq(file_contents)
    char_list = dict_to_list(char_count)
    char_list.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words fouind in the document \n")
    
    for ch in char_list:
        if ch["letter"].isalpha():
            letter = ch["letter"]
            count = ch["num"]
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def get_book(book_path):
    with open(book_path) as f:
        return f.read()

def get_words_count(text):
    words = text.split()
    return len(words)

def words_freq(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def dict_to_list(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"letter": char, "num": char_dict[char]})
    return char_list

def sort_on(dict):
    return dict["num"]

main()