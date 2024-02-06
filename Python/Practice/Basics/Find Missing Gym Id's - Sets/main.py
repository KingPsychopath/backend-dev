def find_missing_ids(first_ids, second_ids):
    first_ids = set(sorted(first_ids))
    second_ids = set(sorted(second_ids))

    print(first_ids)
    print(second_ids)
    unique_id = []
    for i in first_ids:
        if i not in second_ids:
            unique_id.append(i)

    return unique_id

def find_missing_ids2(first_ids, second_ids):
    s1 = set(first_ids)
    s2 = set(second_ids)
    return list(s1 - s2)
