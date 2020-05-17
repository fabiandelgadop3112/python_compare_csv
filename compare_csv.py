csv_origin = open("CSV_1.csv", "r", encoding='utf-8')
csv_modified = open("CSV_2.csv", "r", encoding='utf-8')

list_origin = csv_origin.readlines()
list_modified = csv_modified.readlines()

for line in list_modified:
    if line in list_origin:
        print (f'{line} se encuentra en origen')
    else:
        print (f'{line} no se encuentra en origen')

