#   halvedSections returns a list of lists. For example,
#	    the input "12" would result in
#	    [
#		    [0 1 2 3 4 5 6 7 8 9 10 11 12]
#			[0 1 2 3 4 5 6]
#			[0 1 2 3]
#			[0 1]
#		]
def halved_sections(n):
    rows = []
    i = n
    while i > 0:
        col = []
        for j in range(i+1):
            col.append(j)
        rows.append(col)
        i //= 2
    return rows

print(halved_sections(12))
# Compare this snippet from test.py:

# This has a time complexity of O(n^2) because of the nested for loops.