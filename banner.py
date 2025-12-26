import pyfiglet
import sys
import time

# 24-bit TRUE COLOR (smoothest possible)
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

RESET = "\033[0m"
BOLD = "\033[1m"

# Smooth rainbow gradient
def rainbow_colors(n):
    colors = []
    for i in range(n):
        r = int(127 * (1 + __import__("math").sin(i * 0.15)))
        g = int(127 * (1 + __import__("math").sin(i * 0.15 + 2)))
        b = int(127 * (1 + __import__("math").sin(i * 0.15 + 4)))
        colors.append(rgb(r, g, b))
    return colors

def ultimate_banner(text, speed=0.001):
    banner = pyfiglet.figlet_format(text, font="big")
    colors = rainbow_colors(len(banner))
    i = 0

    for ch in banner:
        if ch != " " and ch != "\n":
            sys.stdout.write(BOLD + colors[i % len(colors)] + ch)
            i += 1
        else:
            sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)

    print(RESET)

if __name__ == "__main__":
    txt = input("Enter banner text: ")
    ultimate_banner(txt)
