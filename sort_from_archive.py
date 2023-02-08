def remove_duplicates(genres):
    without_duplicates = list(set(genres))
    return without_duplicates


def read():
    genres = []
    with open('./genres.txt', "r", encoding='utf-8') as f:
        for line in f:
            genres.append(line.strip())
    remove_duplicates(genres)
    return remove_duplicates(genres)


def genre_sort(genres):
    genres.sort()
    return genres


def write(genres):
    with open("./genres_sorted.sql", "a", encoding='utf-8') as f:
        f.write("INSERT INTO Genre(name)\nVALUES\n")
        for element in genres:
            f.write(f"('{element}'),")
            f.write("\n")


def run():
    clean_genres = genre_sort(read())
    write(clean_genres)
    


if __name__ == '__main__':
    run()