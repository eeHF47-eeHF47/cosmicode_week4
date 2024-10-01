# Task 4: Implement a program that uses a dictionary to count the frequency of each character in a string.
def count_characters(s):
    # Initialize an empty dictionary to store character frequencies
    frequency = {}
    
    # Iterate over each character in the string
    for char in s:
        # Update the frequency count for each character
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

# Example usage:
input_string = "hello world"
result = count_characters(input_string)

print("Character Frequencies:")
for char, count in result.items():
    print(f"'{char}': {count}")
