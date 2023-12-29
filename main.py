def get_book_text(path):
   with open(path) as f:
    return f.read()

def get_num_words(text):
   words = text.split()
   return len(words) 

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
   return d["num"]

def chars_dict_to_sorted_list(letter_list):
    sorted_list = []
    for ch in letter_list:
       sorted_list.append({"char":ch,"num":letter_list[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "books/Frankenstein.txt"
    file_contents = get_book_text(book_path)
    letter_list = count_letters(file_contents)
    sorted_list = chars_dict_to_sorted_list(letter_list)
    print(f"--- Begin report of {book_path}---")
    print(f"{get_num_words(file_contents)} words found in the document")
    for line in sorted_list:
       if not line["char"].isalpha():
          continue
       print(f"The '{line['char']}' character was found {line['num']} times")
    print("--- End report ---")
main()