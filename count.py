# Function to count words in a sentence or paragraph
def count_words(text):
    # Check for empty input
    if not text.strip():
        return 0
    
    # Split the text into words based on spaces
    words = text.split()
    return len(words)

# Function for user input handling
def get_user_input():
    user_text = input("Enter a sentence or paragraph: ")
    return user_text

# Main function to control program flow
def main():
    print("Welcome to Word Counter!")
    
    # Get user input
    text = get_user_input()
    
    # Count words
    word_count = count_words(text)
    
    # Display output
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
