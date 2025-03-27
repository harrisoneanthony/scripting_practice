#!/usr/bin/env python3

def remove_copied(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # remove all instances of "Copied!"
        content = content.replace("Copied!", "")

        with open(filename, 'w') as file:
            file.write(content)

        print(f"All instances of 'Copied!' have been removed from {filename}")

    except FileNotFoundError:
        print(f"Effor:{filename} not found")

    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter filename:")
remove_copied(filename)