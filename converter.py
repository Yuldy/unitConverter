import PySimpleGUI as sg
#Unit Converter Program created by Christian Phan 6/10/22


layout = [
    [sg.Text('Text'), sg.Spin(['item 1,' 'item 2'])], 
    [sg.Button('Button', key = '-BUTTON1-')], 
    [sg.Input()],
    [sg.Text('Test'), sg.Button('Test Button', key = '-BUTTON2-')]] #represents top, middle, bottom row


window = sg.Window('Converter', layout).read() #creates the   window (first parameter represents the tile,)

#window doesn't close after pressing button because of the while loop below:
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        print('button pressed')

    if event == '-BUTTON2-':
        print('something else')

window.close()