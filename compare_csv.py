from unidecode import unidecode

csv_origin = open("CSV_1.csv", "r", encoding='utf-8')
csv_modified = open("CSV_2.csv", "r", encoding='utf-8')

list_origin = csv_origin.readlines()
list_modified = csv_modified.readlines()

list_origin_decode = [unidecode(line) for line in list_origin]

for line in list_modified:
    if line in list_origin:
        print (f'{line} MATCH without modifications')
    
    elif line in list_origin_decode:
        print (f'{line} MATCH removing some accent marks or Ñ character')

    elif unidecode(line) in list_origin:
        print (f'{line} MATCH adding some accent marks or Ñ character')
    
    elif unidecode(line) in list_origin_decode:
        print (f'{line} MATCH adding and removing some accent marks or Ñ character')

    else:
        print (f'{line} DOES NOT match') 
        

    
