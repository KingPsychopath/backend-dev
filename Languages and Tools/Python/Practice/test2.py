def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    res = zipmap(keys[1:], values[1:])
    res[keys[0]] = values[0]
    return res

def zipmap_head(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    else:
        res = {keys[0]: values[0]}
        res.update(zipmap_head(keys[1:], values[1:]))
        return res
    

def zipmap_tail(keys, values, acc={}):
    if len(keys) == 0 or len(values) == 0:
        return acc  # If either list is empty, we return the accumulator, which holds our final result
    else:
        acc[keys[0]] = values[0]  # We add the first key-value pair to the dictionary acc
        # After this line in the first call, acc={1: 4}
        # After this line in the second call, acc={1: 4, 2: 5}
        # After this line in the third call, acc={1: 4, 2: 5, 3: 6}
        return zipmap_tail(keys[1:], values[1:], acc)  
        # We then make the recursive call, passing the rest of the lists and the updated acc
        # In the first call, this is like saying zipmap_tail([2, 3], [5, 6], {1: 4})
        # In the second call, this is like saying zipmap_tail([3], [6], {1: 4, 2: 5})
        # In the third call, this is like saying zipmap_tail([], [], {1:4, 2:5, 3:6})
        # Since the first list is empty, we return the accumulator, which holds our final result

print(zipmap_tail([1, 2, 3], [4, 5, 6]))
# Output:   {1: 4, 2: 5, 3: 6}