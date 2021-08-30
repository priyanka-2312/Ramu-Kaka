from guizero import App, PushButton, Text

import csv

app = App("Display CSV File")

def get_file():
    new_file = app.select_file(filetypes=[["All files", "*.*"], ["CSV documents", "*.csv"]])
    with open('task1.csv.txt','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            file_name=Text(app)
            if line_count == 0:
                file_name.value=f'{", ".join(row)}'
                line_count += 1
            else:
                file_name.value=f'\t{row[0]} {row[1]} ,  {row[2]}.'
                line_count += 1
    









csv_content=Text(app,text="Select csv file: ",size=35,font="Times New Roman")
PushButton(app, command=get_file, text="Select your file")

app.bg="#16A085"

app.display()
