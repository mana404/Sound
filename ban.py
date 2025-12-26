import sys

# Simple ASCII art font (basic block letters)
FONT = {
    'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
    'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
    'C': [" CCC ", "C    ", "C    ", "C    ", " CCC "],
    'D': ["DDD  ", "D  D ", "D  D ", "D  D ", "DDD  "],
    'E': ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
    'F': ["FFFFF", "F    ", "FFF  ", "F    ", "F    "],
    'G': [" GGG ", "G    ", "G GGG", "G   G", " GGG "],
    'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
    'I': [" III ", "  I  ", "  I  ", "  I  ", " III "],
    'J': [" JJJJ", "    J", "    J", "J   J", " JJJ "],
    'K': ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
    'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
    'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
    'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
    'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
    'Q': [" QQQ ", "Q   Q", "Q Q Q", "Q  QQ", " QQQQ"],
    'R': ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
    'S': [" SSS ", "S    ", " SSS ", "    S", " SSS "],
    'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
    'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
    'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
    'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
    'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
    'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
    'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
    ' ': ["     ", "     ", "     ", "     ", "     "]
}

def generate_ascii_art(text):
    """
    Generates simple ASCII art for the given text using a basic font.
    Each character is 5 lines high.
    """
    text = text.upper()  # Convert to uppercase for simplicity
    lines = ['' for _ in range(5)]  # 5 lines per character
    
    for char in text:
        if char in FONT:
            for i in range(5):
                lines[i] += FONT[char][i] + ' '  # Add space between characters
        else:
            # For unknown characters, use space
            for i in range(5):
                lines[i] += FONT[' '][i] + ' '
    
    return '\n'.join(lines)

# Main function
if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = "HELLO WORLD"  # Default text
    
    print(generate_ascii_art(text))