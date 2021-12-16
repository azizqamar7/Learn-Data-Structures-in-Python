# QUESTION 1:
# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


# So we can write a problem statement as:
# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.


# This is the approach

# Create a variable position with the value 0.
# Check whether the number at index position in card equals query.
# If it does, position is the answer and can be returned from the function
# If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
# If the number was not found, return -1.


# This can be sloved using linear search algorithm

def locate_cards(cards, query):
    # Create a variable position with the value 0.
    position = 0

    # set up a loop for repetition
    while position < len(cards):

        # Check if element at the current position matche the query
        if cards[position] == query:

            # Answer found & exit
            return position

        # Increment the position
        position += 1

    return -1


test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
# output = 3
result = locate_cards(**test['input'])
print(result)
