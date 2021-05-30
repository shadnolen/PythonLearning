import PySimpleGUI as sg

income = 0

income = input('Enter Income: ')
income = int(income)

sg.theme('DarkAmber')
layout = [
    [sg.Text('Enter Income'),income = input('Enter Income: ')],
    [sg.Text('Text Line 2')],
    [sg.Button('OK'), sg.Button('Cancel') ]]

    #Create the Window
window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('Your Text', values[0])
window.close
