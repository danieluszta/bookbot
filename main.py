def main():
    path = "./books/frankenstein.txt"
    read_text(path)

def read_text(path):
    with open(path) as f:
      return  print(f.read())





if __name__ == "__main__":
    main()