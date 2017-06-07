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

filename = '/home/eric/projects/intro_programming/notebooks/python_essentials/var_string_num.ipynb'

with open(filename) as f:
    nb_string = f.read()

nb_json = json.loads(nb_string)

# keys: dict_keys(['cells', 'metadata', 'nbformat', 'nbformat_minor'])

# Examine cells.
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

            print('  ohs:', old_highlight_string)
            print('  nhs:', new_highlight_string)
            print('  new code:', code_lines)

            cell['metadata']['highlight_lines'] = new_highlight_string

            print('  new cell:', cell)
            
new_filename = '/home/eric/projects/intro_programming/notebooks/python_essentials/var_string_num_processed.ipynb'
new_nb_string = json.dumps(nb_json)
with open(new_filename, 'w') as f:
    f.write(new_nb_string)
