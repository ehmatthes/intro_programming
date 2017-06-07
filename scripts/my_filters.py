def expand_highlight_lines(highlight_string):
    """Takes a string of form '5,6,8,9,10' or '5,6, 8-10'
    and returns list [5, 6, 8, 9, 10].
    """

    print("\n --- hello template world! ---\n")
    print('highlight_string:', highlight_string)

    expanded_lines = []
    for term in highlight_string.split(','):
        if '-' not in term:
            expanded_lines.append(int(term))
        else:
            start, end = int(term.split('-')[0]), int(term.split('-')[1])
            for new_term in range(start, end + 1):
                expanded_lines.append(new_term)
    return(expanded_lines)
