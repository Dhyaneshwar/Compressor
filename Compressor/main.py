import PySimpleGUI as sg
from zipfile import ZipFile
import pathlib

file_name_label = sg.Text("Enter the compressed filename")
name_input = sg.InputText(key='name')

source_label = sg.Text("Select files to compress")
source_input = sg.InputText(key='source')
source_button = sg.FilesBrowse("Choose")

destination_label = sg.Text("Select destination folder")
destination_input = sg.InputText(key='destination')
destination_button = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output')

window = sg.Window(
                    "My File Zipper", 
                    layout=[
                        [file_name_label, name_input],
                        [source_label,source_input,source_button], 
                        [destination_label,destination_input,destination_button], 
                        [compress_button, output_label]]
                )

while True:
    event, values = window.read()

    match event:
        case 'Compress':
            file_name = values['name'].strip()
            compress_files = values['source'].split(';')
            compress_destination = values['destination']

            if file_name == '' or compress_files == '' or compress_destination == '':
                print('Please provide valid inputs')
                continue

            compress_path = pathlib.Path(compress_destination, f'{file_name}.zip')
            with ZipFile(compress_path, 'w') as file:
                for file_path in compress_files:
                    file_path = pathlib.Path(file_path)
                    file.write(file_path, arcname=file_path.name)

            window['name'].update(value='')
            window['source'].update(value='')
            window['destination'].update(value='')
            window['output'].update(value='Files are compressed successfully')

        case sg.WIN_CLOSED:
            break

window.close()