def main():
        book_path = "./books/frankenstein.txt"
        text = get_book_text(book_path)
        word_len = count_words(text)
        #print(word_len)
        char_count = count_characters(text)
        #print(char_count)
        report = print_report(word_len, char_count)
        print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    for char in text:
        character = char.lower()
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count

def print_report(count, count_frequency):
    header = "--- Begin report of books/frankenstein.txt ---\n"
    words = f"{count} words found in the document \n"
    
    def sort_frequency(frequency):
        dict_list = []
        for key in frequency:
            temp_dict = {}
            if key.isalpha():
                temp_dict["char"] = key
                temp_dict["count"] = frequency[key]
                dict_list.append(temp_dict)
        
        def sort_on(dict):
            return dict["count"]
        
        dict_list.sort(reverse=True, key=sort_on)
        return dict_list
    frequency_report = ""
    for dict in sort_frequency(count_frequency):
        key = dict["char"]
        val = dict["count"]
        frequency_report += f"The {key} character was found {val} times\n"
    return header + words + '\n' + frequency_report + "--- End report ---"
        

main()