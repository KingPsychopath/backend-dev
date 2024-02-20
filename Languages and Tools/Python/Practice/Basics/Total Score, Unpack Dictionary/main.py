def merge(dict1, dict2):
    merged = {**dict1, **dict2}
    print(merged)
    return merged

def merge2(dict1, dict2):
    merged_dict = {}
    for k in dict1:
        merged_dict[k] = dict1[k] # didn't know equating a key to a value would add it to the dictionary
    for k in dict2:
        merged_dict[k] = dict2[k]
    return merged_dict

def total_score(score_dict):
    total = 0
    for i in score_dict:
        total += score_dict[i] 
    return total

'''
The double asterisk "**" is known as the dictionary unpacking operator in Python. It is used to unpack the keys and values from a dictionary into a new dictionary.

So when you use "**" before a dictionary like this: **dict1, Python will break down the dictionary into its individual key: value pairs.

Now, when you use this unpacking operator with multiple dictionaries within the {} braces like so: {**dict1, **dict2}, you're telling Python to unpack, or break down, the individual key: value pairs from both dictionaries and use them to create a new dictionary.

This is how Python merges two dictionaries together into a new one.


'''