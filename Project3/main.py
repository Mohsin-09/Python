import num2words

def number_to_words():
    try:
        # Input a numeric value
        num = int(input("Enter a number: "))
        # Convert to words
        words = num2words.num2words(num)
        print(f"In words: {words}")
    except ValueError:
        print("Please enter a valid numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
number_to_words()
