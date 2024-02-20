def filter_messages(messages):
    filtered_messages = []
    dang_count = []

    filtered_word = 'dang'

    for message in messages:
        words = message.split()
        dang_counter = 0
        print(words)
        
        for word in words[:]:
            if word == filtered_word:
                dang_counter += 1
                words.remove(word)

        sentence = ' '.join(words)
        filtered_messages.append(sentence)
        dang_count.append(dang_counter)

    return filtered_messages, dang_count



def filter_messages2(messages):
    filtered_messages = []
    words_removed = []
    for message in messages:
        words = message.split()
        new_words = []
        removed = 0
        for word in words:
            if word == "dang":
                removed += 1
            else:
                new_words.append(word)
        filtered_messages.append(" ".join(new_words))
        words_removed.append(removed)

    return filtered_messages, words_removed

'''
In this context, using list.remove() is more appropriate because you want to remove a specific value (filtered_word) from the list. The remove() method removes the first matching value from the list, which is exactly what you need here.

The del statement, on the other hand, removes an item at a specific index, not a specific value. If you know the index of the item you want to remove, you could use del, but in this case, you don't know the index of filtered_word in advance.

However, it's worth noting that both del and remove() modify the list in-place, which can lead to unexpected results when iterating over the list. To avoid this, you're correctly creating a copy of the list with words[:] before the inner loop.

Here's the relevant part of your code with remove():



The slice operator [:] is used in this code to create a copy of the words list.

In Python, when you iterate over a list and modify it at the same time, it can lead to unexpected behavior. This is because the iteration is based on the original length of the list, and modifying the list during iteration can cause elements to be skipped or processed incorrectly.

By using the slice operator [:], a copy of the words list is created. This ensures that the iteration is based on the original length of the list, and any modifications made to the list during the iteration will not affect the iteration itself.

Here's an example to illustrate this:

words = ['apple', 'banana', 'cherry']

# Without using the slice operator
for word in words:
    if word == 'banana':
        words.remove(word)

print(words)  # Output: ['apple', 'cherry']

# Using the slice operator
for word in words[:]:
    if word == 'banana':
        words.remove(word)

print(words)  # Output: ['apple', 'cherry']


In the first example, without using the slice operator, the iteration skips the element 'cherry' because the list is modified during the iteration. In the second example, using the slice operator, a copy of the list is made, and the iteration is based on the original length of the list, resulting in all elements being processed correctly.The slice operator [:] is used in this code to create a copy of the words list.

In Python, when you iterate over a list and modify it at the same time, it can lead to unexpected behavior. This is because the iteration is based on the original length of the list, and modifying the list during iteration can cause elements to be skipped or processed incorrectly.

By using the slice operator [:], a copy of the words list is created. This ensures that the iteration is based on the original length of the list, and any modifications made to the list during the iteration will not affect the iteration itself.
'''