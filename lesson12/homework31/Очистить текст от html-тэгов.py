import codecs


def html_cleaner(first_file,clean_file):
    first_file = codecs.open(first_file, "r", "UTF-8")
    clean_file = codecs.open(clean_file, "w", "UTF-8")
    lst = list(first_file.read())
    i = 0
    while i < len(lst):
        if lst[i] == "<":
            while lst[i] != ">":
                del lst[i]
        i += 1
    i = 0
    while i < len(lst):
        if lst[i] == '>':
            del lst[i]
        else:
            i += 1
    lst = "".join(lst)
    clean_file.writelines(lst)
    first_file.close()
    clean_file.close()


html_cleaner("draft.html","clean.txt")