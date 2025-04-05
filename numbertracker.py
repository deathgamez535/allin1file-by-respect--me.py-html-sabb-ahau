import re

def track_numbers_in_text(text):
    """
    Track and count the occurrences of numbers in the given text.

    Parameters:
    text (str): The input text where numbers need to be tracked.

    Returns:
    dict: A dictionary with numbers as keys and their counts as values.
    """
    # Use regular expression to find all numbers in the text
    numbers = re.findall(r'\d+', text)  # Finds all digit sequences

    # Initialize an empty dictionary to store the count of each number
    number_count = {}

    # Count occurrences of each number
    for number in numbers:
        number_count[number] = number_count.get(number, 0) + 1

    return number_count

def track_numbers_in_file(filename):
    """
    Track and count numbers in a file.

    Parameters:
    filename (str): The path to the file that contains text with numbers.

    Returns:
    dict: A dictionary with numbers as keys and their counts as values, or None if file is not found.
    """
    try:
        # Open and read the file content
        with open(filename, 'r') as file:
            text = file.read()

        # Call the track_numbers_in_text function to get the count of numbers in the text
        return track_numbers_in_text(text)

    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return None

def track_numbers_in_list(number_list):
    """
    Track and count the occurrences of numbers in a list.

    Parameters:
    number_list (list): A list of numbers.

    Returns:
    dict: A dictionary with numbers as keys and their counts as values.
    """
    number_count = {}

    for number in number_list:
        number_count[number] = number_count.get(number, 0) + 1

    return number_count

def display_results(count_dict):
    """
    Display the results in a user-friendly way.

    Parameters:
    count_dict (dict): The dictionary containing numbers and their counts.
    """
    if count_dict:
        print("Number Occurrences:")
        for number, count in count_dict.items():
            print(f"Number {number}: {count} time(s)")
    else:
        print("No numbers tracked.")

# Example Usage
if __name__ == "__main__":
    # Example text to track numbers in
    sample_text = """Here are some order numbers: 123, 456, 123, 789, 123.
    We also have invoice number 123, and the customer ID is 456."""

    # Tracking numbers in text
    print("\nTracking numbers in sample text:")
    number_count_in_text = track_numbers_in_text(sample_text)
    display_results(number_count_in_text)

    # Example list of numbers to track
    number_list = [123, 456, 123, 789, 123, 101, 202, 456, 123]
    print("\nTracking numbers in list:")
    number_count_in_list = track_numbers_in_list(number_list)
    display_results(number_count_in_list)

    # Example of tracking numbers in a file (create your own file first)
    filename = "sample_numbers.txt"
    print("\nTracking numbers in file:")
    number_count_in_file = track_numbers_in_file(filename)
    display_results(number_count_in_file)
