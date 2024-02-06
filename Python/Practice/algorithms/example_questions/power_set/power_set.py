def power_set(input_set):
    # ?
    print(input_set)
    if len(input_set) == 0:
        return [[]]

    final_subset = []

    current_subset = power_set(input_set[1:])
    print(f'{current_subset} <=== RETURNED')
    for subset in current_subset:
        print(f'INDEX[{current_subset.index(subset)}]                Input Set: {input_set}')
        final_subset.append([input_set[0]] + subset)
        print(f'   APPEND [{input_set[0]}] + {subset} ===>  {final_subset}')
        final_subset.append(subset)
        print(f'   APPEND SUBSET {subset} ===>  {final_subset}')     
    return final_subset
        


# don't touch below this line


def test(input_set):
    result = power_set(input_set)
    print(f"Number of subsets of {input_set}: {len(result)}")
    print("====================================")


def main():
    for i in range(1, 5):
        nums = list(range(1, i))
        test(nums)


main()


def power_set2(input_set):
    if len(input_set) == 0:
        return [[]]

    subsets = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subsets