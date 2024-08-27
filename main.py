import string
def main():
    path = "./books/frankenstein.txt"
    print(read_text(path))
    print(count_words(read_text(path)))
    print(word_instances(read_text(path)))

def read_text(path):
    with open(path) as f:
      return f.read()

def count_words(text):
    new_list = text.split()
    return len(new_list)

def word_instances(text):
    instances_dict = {}
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        instances_dict[letter] = text.lower().count(letter)
    return instances_dict



if __name__ == "__main__":
    main()