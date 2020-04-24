from pyfiglet import Figlet

def banner(text):
    font = Figlet(font='slant')
    print(font.renderText(text))


banner("Willy Wangky")

