import csv

with open('data/books.csv','r',encoding='utf-8') as rf:
    reader = csv.reader(rf)
    with open('data/books2.csv','w',newline='',encoding='utf-8')as wf:
        writer = csv.writer(wf,delimiter='\t')
        for row in reader:
            print('|'.join(row))
            writer.writerow(row)