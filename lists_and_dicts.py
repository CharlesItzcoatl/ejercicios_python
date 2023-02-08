def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Charls", "lastname": "Itzcoatl"}

    super_list = [
        {"firstname": "Charls", "lastname": "Itzcoatl"},
        {"firstname": "Peludi", "lastname": "García"},
        {"firstname": "Jesucristo", "lastname": "Superstar"},
        {"firstname": "Erasmo", "lastname": "Valverde"},
        {"firstname": "Alberto", "lastname": "Vargas"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.2, 45.67]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()