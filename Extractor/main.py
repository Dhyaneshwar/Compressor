import PySimpleGUI as sg
from zipfile import ZipFile
import pathlib

source_label = sg.Text("Select zip file")
source_input = sg.InputText(key='source')
source_button = sg.FilesBrowse("Choose")

destination_label = sg.Text("Select destination folder")
destination_input = sg.InputText(key='destination')
destination_button = sg.FolderBrowse("Choose")

compress_button = sg.Button("Extract")
output_label = sg.Text(key='output')

window = sg.Window(
                    "My File Extractor", 
                    layout=[
                        [source_label,source_input,source_button], 
                        [destination_label,destination_input,destination_button], 
                        [compress_button, output_label]]
                )

while True:
    event, values = window.read()
    match event:
        case "Extract":
            compress_file = values['source']
            extract_destination = values['destination']
            with ZipFile(compress_file, 'r') as file:
                file.extractall(extract_destination)
            
        case sg.WIN_CLOSED:
            break

window.close()