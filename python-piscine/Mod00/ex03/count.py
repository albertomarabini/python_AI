import string

def text_analyzer(text=None):
    """
    Analyze a given text and display the count of its upper-case characters,
    lower-case characters, punctuation characters, and spaces.

    Parameters:
    text (str, optional): The text to be analyzed. If not provided, the user
    will be prompted to enter a text.

    Raises:
    AssertionError: If the argument provided is not a string.

    Returns:
    None: This function doesn't return anything. It only prints the analysis.
    """
    if text is None:
        text = input("What is the text to analyze?\n>> ")

    if not isinstance(text, str):
        raise AssertionError("argument is not a string")

    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punctuation = sum(1 for char in text if char in string.punctuation)
    spaces = text.count(' ')

    print(f"The text contains {len(text)} character(s):"
          f"\n- {upper} upper letter(s)"
          f"\n- {lower} lower letter(s)"
          f"\n- {punctuation} punctuation mark(s)"
          f"\n- {spaces} space(s)")

# Example usage
if __name__ == "__main__":
    from count import text_analyzer
    text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
