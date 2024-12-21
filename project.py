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
window.config( )


label_1 = Label( window, text = 'Enter any Text :' )
label_1.place( x = 35, y = 100)

entry_1 = Entry( window, )
entry_1.place( x = 290, y = 250 - 140 )

upper_button = Button( window,
                      command = upper_func)
upper_button.place( x = 550, y = 140 )

capitalize_button = Button( window,
                           command = capitalize_func)
capitalize_button.place( x = 540, y = 240 )

lower_button = Button( window,
                      command = lower_func)
lower_button.place( x = 550, y = 340 )


output_label = Label( window, )
output_label.place( x = 150, y = 380 )





window.mainloop()