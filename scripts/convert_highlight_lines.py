"""Convert from the old way of designating lines for highlighting, to the new way.

Old way: First line of a program is
    ###highlight=[6,7,8]

New way: Add an attribute to cell metadata
{
  'highlight_lines': '4,5',
  'trusted': true
}

  This allows strings including ranges like '4,5,8-12' as well.

"""

import json


def convert_file(filename):
    """Convert old highlight lines format to new using cell metadata."""

    with open(filename) as f:
        nb_string = f.read()

    nb_json = json.loads(nb_string)

    # keys: dict_keys(['cells', 'metadata', 'nbformat', 'nbformat_minor'])

    # Examine cells.
    try:
        for cell in nb_json['cells']:
            # Examine first line of each code cell.
            if cell['cell_type'] == 'code':
                code_lines = cell['source']
                if '###highlight=' in code_lines[0]:
                    print("\n--source--\n", code_lines)
                    print("  -- metadata --", cell['metadata'])
                    print("  original cell:", cell)

                    # Remove the first line, convert it to new format and add to metadata.
                    #  Need to subtract 1 from each line number, because removing first line
                    #  that held the old highlight string.
                    old_highlight_string = code_lines.pop(0)
                    new_highlight_string = old_highlight_string[14:-2]
                    correct_line_nums = [int(line_num) - 1 for line_num in new_highlight_string.split(',')]
                    new_highlight_string = ','.join([str(line_num) for line_num in correct_line_nums])

                    print('  ohs:', old_highlight_string)
                    print('  nhs:', new_highlight_string)
                    print('  new code:', code_lines)

                    cell['metadata']['highlight_lines'] = new_highlight_string

                    print('  new cell:', cell)

        # Rewrite ipynb file.
        new_nb_string = json.dumps(nb_json)
        with open(filename, 'w') as f:
            f.write(new_nb_string)

    except KeyError:
        print("\n-- Notebook has no cells: --", filename)


# filename = '/home/eric/projects/intro_programming/notebooks/python_essentials/var_string_num.ipynb'
# convert_file(filename)
