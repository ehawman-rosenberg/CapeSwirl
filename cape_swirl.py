import re
import sys
import os

default = {
    "Name": "Default",
    "Palette": {
        "Background": "282a36",
        "Selection": "44475a",
        "Foreground": "f8f8f2",
        "Comment": "6272a4",
        "Cyan": "8be9fd",
        "Green": "50fa7b",
        "Orange": "ffb86c",
        "Pink": "ff79c6",
        "Purple": "bd93f9",
        "Red": "ff5555",
        "Yellow": "f1fa8c",
        "AnsiBlack": "21222c",
        "AnsiBrightRed": "ff6e6e",
        "AnsiBrightGreen": "69ff94",
        "AnsiBrightYellow": "ffffa5",
        "AnsiBrightBlue": "d6acff",
        "AnsiBrightMagenta": "ff92df",
        "AnsiBrightCyan": "a4ffff",
        "AnsiBrightWhite": "ffffff",
    },
}

one = {
    "Name": "One",
    "Palette": {
        "Background": "22212c",
        "Selection": "454158",
        "Foreground": "f8f8f2",
        "Comment": "7970a9",
        "Cyan": "80ffea",
        "Green": "8aff80",
        "Orange": "ffb86c",
        "Pink": "ff80bf",
        "Purple": "9580ff",
        "Red": "ff9580",
        "Yellow": "ffff80",
        "AnsiBlack": "1b1a23",
        "AnsiBrightRed": "ffaa99",
        "AnsiBrightGreen": "a2ff99",
        "AnsiBrightYellow": "ffff99",
        "AnsiBrightBlue": "aa99ff",
        "AnsiBrightMagenta": "ff99cc",
        "AnsiBrightCyan": "99ffee",
        "AnsiBrightWhite": "ffffff",
    },
}

two = {
    "Name": "Two",
    "Palette": {
        "Background": "2a212c",
        "Selection": "544158",
        "Foreground": "f8f8f2",
        "Comment": "9f70a9",
        "Cyan": "80ffea",
        "Green": "8aff80",
        "Orange": "ffca80",
        "Pink": "ff80bf",
        "Purple": "9580ff",
        "Red": "ff9580",
        "Yellow": "ffff80",
        "AnsiBlack": "1b1a23",
        "AnsiBrightRed": "ffaa99",
        "AnsiBrightGreen": "a2ff99",
        "AnsiBrightYellow": "ffff99",
        "AnsiBrightBlue": "aa99ff",
        "AnsiBrightMagenta": "ff99cc",
        "AnsiBrightCyan": "99ffee",
        "AnsiBrightWhite": "ffffff",
    },
}

three = {
    "Name": "Three",
    "Palette": {
        "Background": "0b0d0f",
        "Selection": "414d58",
        "Foreground": "f8f8f2",
        "Comment": "708ca9",
        "Cyan": "80ffea",
        "Green": "8aff80",
        "Orange": "ffca80",
        "Pink": "ff80bf",
        "Purple": "9580ff",
        "Red": "ff9580",
        "Yellow": "ffff80",
        "AnsiBlack": "1b1a23",
        "AnsiBrightRed": "ffaa99",
        "AnsiBrightGreen": "a2ff99",
        "AnsiBrightYellow": "ffff99",
        "AnsiBrightBlue": "aa99ff",
        "AnsiBrightMagenta": "ff99cc",
        "AnsiBrightCyan": "99ffee",
        "AnsiBrightWhite": "ffffff",
    },
}

exports = (one, two, three)


def main():
    """Main program"""
    directory = "input"

    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            with open(f, "r") as open_file:
                file = open_file.read()

        for export in exports:
            for key, value in default["Palette"].items():
                swirl = re.compile(re.escape(value), re.IGNORECASE)
                file = swirl.sub(export["Palette"][key], file)
            with open(
                os.path.join("output", export["Name"] + filename), "w+"
            ) as open_file:
                open_file.write(file)


if __name__ == "__main__":
    main()
