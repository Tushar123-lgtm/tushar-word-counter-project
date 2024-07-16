def word_counter(text):
    """
    Function to count the number of words in a given text.

    Parameters:
    text (str): The input text provided by the user.

    Returns:
    int: The number of words in the input text.
    """
    words = text.split()  # Splitting the text into words based on whitespace
    return len(words)  # Counting the number of words

def main():
    print("Welcome to the Word Counter project of Tushar!")

    while True:
        try:
            text = input("\nPlease Enter a sentence or paragraph (or  Enter 'exit' to quit): ")

            if text.lower() == 'exit':
                print("Thank you for using the Word Counter. Goodbye!")
                break

            # Counting words
            num_words = word_counter(text)
            print(f"\nNumber of words in the text: {num_words}")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break

        except Exception as e:
            print(f"\nError occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()
