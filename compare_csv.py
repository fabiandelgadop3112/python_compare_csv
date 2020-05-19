from unidecode import unidecode

line_break = '\n'
csv_origin = open("CSV_1.csv", "r", encoding='utf-8')
csv_modified = open("CSV_2.csv", "r", encoding='utf-8')
out_file = open("results.csv", "w" , encoding='utf-8')

list_origin = csv_origin.readlines()
list_modified = csv_modified.readlines()

list_origin_decode = [unidecode(line) for line in list_origin]

line_number = 0

for line in list_modified:

    if line in list_origin:

        out_line = f'{line.rstrip(line_break)},MATCH without modifications{line_break}'

    elif line in list_origin_decode:

        out_line =  f'{line.rstrip(line_break)},MATCH removing some accent marks or Ñ character{line_break}'

    elif unidecode(line) in list_origin:

        out_line =  f'{line.rstrip(line_break)},MATCH adding some accent marks or Ñ character{line_break}'

    elif unidecode(line) in list_origin_decode:

        out_line =  f'{line.rstrip(line_break)},MATCH adding and removing some accent marks or Ñ character{line_break}'

    else:
        out_line =  f'{line.rstrip(line_break)},DOES NOT match{line_break}'

    out_file.write(out_line)
    line_number += 1    

print(f'{line_number} lines was processed OK')
print(f'File {out_file.name} was created succesfully')

    
