
def main():
    path= "./books/frankenstein.txt"
    book_text= get_book_text(path)
    number_of_words= count_words(book_text)
    character_report= count_char_appearance(book_text)
    sorted_character_report= char_count_to_sorted_list(character_report)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in document\n")
    print_char_count_nicely(sorted_character_report)
    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()
    
def count_words(book_text):
    book_text_array= book_text.split()
    return len(book_text_array)

def count_char_appearance(book_text):
    word_appearance={}

    all_characters= get_all_characters_in_book(book_text)
    for character_in_set in all_characters:
        num_appearance=0
        for character_in_book in book_text:
            if character_in_book.lower() == character_in_set:
                num_appearance+= 1
        word_appearance[character_in_set]= num_appearance
    return word_appearance

def get_all_characters_in_book(book_text):
    characters= set()
    for character in book_text:
        characters.add(character.lower())
    return characters

def sort_on(d):
    return d["num"]

def char_count_to_sorted_list(character_dict):
    sorted_list= []
    for key in character_dict:
        if(key.isalpha()):
            sorted_list.append({ "char": key , "num": character_dict[key]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

def print_char_count_nicely(character_list):
    for char in character_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times")


main()