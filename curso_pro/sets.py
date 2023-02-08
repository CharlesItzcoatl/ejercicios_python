def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def with_sets(some_list):
    without_duplicates = list(set(some_list))
    
    return without_duplicates        


def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))
    print(random_list)
    print(with_sets(random_list))


if __name__ == '__main__':
    run()