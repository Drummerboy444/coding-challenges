from encrypter import Encrypter


def encrypt(message, dimensions, direction):
    width = dimensions[0]
    height = dimensions[1]

    formatted_message = format_message(message, width, height)
    grid = build_grid(formatted_message, width, height)
    return Encrypter(grid).encrypt(direction)


def format_message(message, width, height):
    stripped_message = ""
    for character in message:
        if character.isalpha():
            stripped_message += character

    uppercased_message = stripped_message.upper()

    grid_size = width * height
    return uppercased_message + ((grid_size - len(uppercased_message)) * "X")


def build_grid(message, width, height):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            character_index = (i * width) + j
            row.append(message[character_index])
        grid.append(row)
    return grid
