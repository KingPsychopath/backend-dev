from functools import reduce
def get_median_font_size(font_sizes):
    if not font_sizes:
        return None

    sorted_fonts = sorted(font_sizes) # O(nlogn) - sort in scope of function, not in place (not modifying original list) with .sort()
    n = len(sorted_fonts)
    if n % 2 == 0:
        even_average = reduce(lambda x, y: (x + y) / 2, (sorted_fonts[n // 2 - 1], sorted_fonts[n // 2]))
        return even_average
    return sorted_fonts[n // 2]  

def get_median_font_size2(font_sizes):
    if len(font_sizes) == 0:
        return None
    sorted_sizes = sorted(font_sizes)
    n = len(sorted_sizes)
    if n % 2 == 0:
        return (sorted_sizes[n // 2 - 1] + sorted_sizes[n // 2]) / 2
    else:
        return sorted_sizes[n // 2]