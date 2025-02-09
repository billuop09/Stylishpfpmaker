# Simple Hello World script with user input

def main():
    # Print a greeting message
    print("Hello, World!")
    
    # Ask the user for their name
    name = input("What's your name? ")
    
    # Print a personalized greeting
    print(f"Nice to meet you, {name}!")

# Check if this script is being run directly
if __name__ == "__main__":
    main()