def weight_on_planets():
    """Prompts the user for their weight on Earth
    and then prints out the weight on Mars and Jupiter"""
    weight = int(input("What do you weigh on earth? "))
    print(
        "\n"
        "On Mars you would weigh", weight * 0.38, "pounds.\n"
        "On Jupiter you would weigh", weight * 2.34, "pounds."
    )


if __name__ == '__main__':
    weight_on_planets()
