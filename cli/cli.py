"""
Command line interface for the program.
"""
import argparse

PROGRAM_NAME = "SD Card File Manager"  # TODO: Think of a more accurate name
PROGRAM_DESCRIPTION = "Download audio files from a URL. Move later to an SD " \
                      "card or external storage."

COMMANDS = (
    "add", "rm", "download"
)


def main():
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME,
                                     description=PROGRAM_DESCRIPTION)
    parser.add_argument("Command", choices=COMMANDS, type=str,
                        metavar="command", nargs=1, action='store')

# Import argparse
# ArgumentParser class
    # "Add"
        # "Service" (e.g. youtube)
    # "Remove"
        # URL
    # Download
# Build parse
