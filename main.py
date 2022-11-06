from scanner.plateinfo import searchPlate
import os

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

class tools:
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

tools.clear()


def allColors():
    for color in colors.__dict__:
        if color != 'end':
            print(f"{colors.__dict__[color]}{color}{colors.end}")


print(f"""{colors.blue}
 ▐ ▄ .▄▄ · ▄▄▌ ▐ ▄▌ ▄▄▄·▄▄▌   ▄▄▄· ▄▄▄▄▄▄▄▄ .
•█▌▐█▐█ ▀. ██· █▌▐█▐█ ▄███•  ▐█ ▀█ •██  ▀▄.▀·
▐█▐▐▌▄▀▀▀█▄██▪▐█▐▐▌ ██▀·██▪  ▄█▀▀█  ▐█.▪▐▀▀▪▄
██▐█▌▐█▄▪▐█▐█▌██▐█▌▐█▪·•▐█▌▐▌▐█ ▪▐▌ ▐█▌·▐█▄▄▌
▀▀ █▪ ▀▀▀▀  ▀▀▀▀ ▀▪.▀   .▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀ 
{colors.end}This is a script to check license plates in {colors.underline + colors.bold}NSW ONLY{colors.end}.""")

while True:
    plate = input(f"\n[{colors.yellow}?{colors.end}] Enter plate number: ")
    searchPlate(plate.upper())
