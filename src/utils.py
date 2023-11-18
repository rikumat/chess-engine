letter_to_number = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7
}

number_to_letter = {number:letter for letter, number in letter_to_number.items()}


def square_to_coordinates(square):
        x=letter_to_number[square[0]]
        y=8-int(square[1])
        return (y, x)

def coordinates_to_square(x, y):
    letter=number_to_letter[y]
    number=8-x
    return letter+str(number)

