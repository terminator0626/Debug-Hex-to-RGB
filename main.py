def hex_to_rgb(hex_color):
    
    # Check if the input is a valid hexadecimal color string
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise ValueError("not a hex color string")

    # Convert the hexadecimal values to integers
    red = int(hex_color[:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:], 16)

    return red, green, blue


def is_hexadecimal(hex_string):

    try:
        int(hex_string, 16)
        return True
    except (ValueError, TypeError):
        return False


        
