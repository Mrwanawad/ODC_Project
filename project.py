from tkinter import *

def upper_func() :
    
    text = entry_1.get()
    output_label['text'] = 'Output : ' + text.upper()

def capitalize_func() :
    
    text = entry_1.get()
    output_label['text'] = 'Output : ' + text.capitalize()
    
def lower_func() :
    
    text = entry_1.get()
    output_label['text'] = 'Output : ' + text.lower()    


window = Tk()
window.geometry( '900x400')
window.resizable(False, False)
window.config( bg = 'LemonChiffon2' )


label_1 = Label( window, text = 'Enter any Text :', font = ('Times New Roman', 25), fg = 'red4', bg = 'LemonChiffon2' )
label_1.place( x = 35, y = 100)

entry_1 = Entry( window, font = ('Times New Roman', 18), fg = 'red4', bg = 'snow2', width = 15 )
entry_1.place( x = 290, y = 250 - 140 )

upper_button = Button( window, text = 'Click to show upper\n version of your name', font = ('Times New Roman', 14), fg = 'navy', bg = 'snow2', width = 18,
                      command = upper_func)
upper_button.place( x = 550, y = 140 )

capitalize_button = Button( window, text = 'Click to show capitalized\n version of your name', font = ('Times New Roman', 14), fg = 'navy', bg = 'snow2', width = 20,
                           command = capitalize_func)
capitalize_button.place( x = 540, y = 240 )

lower_button = Button( window, text = 'Click to show lower\n version of your name', font = ('Times New Roman', 14), fg = 'navy', bg = 'snow2', width = 18,
                      command = lower_func)
lower_button.place( x = 550, y = 340 )


output_label = Label( window, text = 'Output :', font = ('Times New Roman', 32), fg = 'navy', bg = 'LemonChiffon2' )
output_label.place( x = 150, y = 380 )





window.mainloop()