import string
def main():
    path = "./books/frankenstein.txt"
    red_text = read_text(path)
    word_count = count_words(red_text)
    count_letter_instances = word_instances(red_text)
    report(word_count,count_letter_instances)

def read_text(path):
    with open(path) as f:
      return f.read()

def count_words(text):
    new_list = text.split()
    return len(new_list)
def sort_on(dict):
    return dict['count']

def word_instances(text):
    instances_dict = {}
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
       instances_dict[letter] = text.lower().count(letter)
    instances_list = [{"letter":item, "count":instances_dict[item]} for item in instances_dict]
    instances_list.sort(reverse=True,key=sort_on)
    return instances_list
def report(word_count, count_letter_instances):
    print("---Begin report of books/frankenstein.txt---")
    print(f"{word_count} words found in the document")
    print("")
    for item in count_letter_instances:
        print(f"The {item["letter"]} character was found {item["count"]} times")
    print("---End of report---")



if __name__ == "__main__":
    main()