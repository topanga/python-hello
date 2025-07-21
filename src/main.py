# This script prompts the user for their name and greets them.
# If no name is entered, it notifies the user that no name was provided.
def main():
    name = input("Enter the name of the user: ")
    if not name:
        print("No name provided.")
    else:
        print(f"Hello {name}")

if __name__ == "__main__":
    main()
