import string

dracula_list = []
dracula_dict = {}
dracula_pair = {}

with open("dracula.txt") as dracula:
    dracula_book = dracula.read()
    dracula_book = dracula_book.lower()

    for punc in string.punctuation:
        dracula_book = dracula_book.replace(punc, "")
        dracula_book = dracula_book.replace(",", "")
        dracula_book = dracula_book.replace("\n", "")
        dracula_book = dracula_book.replace(":", "")
        dracula_book = dracula_book.replace("/", "")

    dracula_book = dracula_book.split(" ")
    dracula_list = list(dracula_book)

    for word in dracula_list:
        if not word:
            continue
        if word in dracula_dict:
            dracula_dict[word] += 1
        else:
            dracula_dict[word] = 1

    drac_words = list(dracula_dict.items())
    drac_words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(drac_words))):
        print(drac_words[i])



    # dracula_book = dracula_book.replace("!", "")
    # #dracula_book = dracula_book.replace(""", "")
    # dracula_book = dracula_book.replace("#", "")
    # dracula_book = dracula_book.replace("$", "")
    # dracula_book = dracula_book.replace("%", "")
    # dracula_book = dracula_book.replace("&", "")
    # dracula_book = dracula_book.replace("'", "")
    # dracula_book = dracula_book.replace("(", "")
    # dracula_book = dracula_book.replace(")", "")
    # dracula_book = dracula_book.replace("*", "")
    # dracula_book = dracula_book.replace("+", "")
    # dracula_book = dracula_book.replace(",", "")
    # dracula_book = dracula_book.replace("-", "")
    # dracula_book = dracula_book.replace(".", "")
    # dracula_book = dracula_book.replace(";", "")
    # dracula_book = dracula_book.replace("<", "")
    # dracula_book = dracula_book.replace("=", "")
    # dracula_book = dracula_book.replace(">", "")
    # dracula_book = dracula_book.replace("?", "")
    # dracula_book = dracula_book.replace("@", "")
    # dracula_book = dracula_book.replace("[", "")
    # dracula_book = dracula_book.replace("\", "")
    # dracula_book = dracula_book.replace("]", "")
    # dracula_book = dracula_book.replace("^", "")
    # dracula_book = dracula_book.replace("_", "")
    # dracula_book = dracula_book.replace("`", "")
    # dracula_book = dracula_book.replace("{", "")
    # dracula_book = dracula_book.replace("|", "")
    # dracula_book = dracula_book.replace("}", "")
    # dracula_book = dracula_book.replace("~", "")
    # dracula_book = dracula_book.replace(f"\n", "")
    # dracula_list = list(dracula_book.items())
    # print(dracula_list)
