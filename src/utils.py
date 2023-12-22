letter_to_number = {
    "h":7,
    "g":6,
    "f":5,
    "e":4,
    "d":3,
    "c":2,
    "b":1,
    "a":0
}
number_to_letter = {number:letter for letter, number in letter_to_number.items()}

def square_to_coordinates(square):
    """
    convert chess square to coordinates (y, x) of a 2-dimensional list.
    """
    x=letter_to_number[square[0]]
    y=8-int(square[1])
    return (y, x)

def coordinates_to_square(coordinates):
    """
    convert coordinates (y, x) to chess square.
    """
    letter=number_to_letter[coordinates[1]]
    number=8-coordinates[0]
    return letter+str(number)
        