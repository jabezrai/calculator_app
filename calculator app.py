import tkinter as tk
reset_display = False
ans = 0

    #function for the buttons
def click(action):
    global reset_display,ans

    current = display.get() #variable for storing information input recently
    button_txt = action.widget["text"] #variables storing the button clicked

    #assigning C to clear entry
    if button_txt == "C":
        display.delete(0, tk.END)
        display.insert(tk.END, '0')
        reset_display = False

    #assigning % as /100 to present integers as percentage in decimals
    elif button_txt == "=":
        try:
            expression = current.replace('%','/100')
            result = eval(expression)
            ans=result
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            reset_display = True

    #catches errors during calculation and displays "error" instead of letting the error interrupt the program.
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, 'error')
            reset_display = True

    elif button_txt == 'Ans':
        display.delete(0, tk.END)
        display.insert(tk.END, str(ans))

    # resets entry when reset_display is True
    else:
        if reset_display:
            display.delete(0, tk.END)
            current = ''
            reset_display = False

        #prevents displaying 000 in entry
        if current == '0':
            current = ''

        #avoid 2 same operators
        operators = '+-*/%'
        if current and current[-1] in operators and button_txt in operators:
            current = current[:-1]

        #avoid starting with certain operators
        if current == '' and button_txt == '*/%':
            return

        #update entry widget with result only after expression
        display.delete(0, tk.END)
        display.insert(tk.END, current + button_txt)



#importing GUI
root = tk.Tk()
root.configure(bg='gray25')
root.title("Calculator")
root.geometry("400x500")
root.resizable(False,False)

#Frame for input display
display = tk.Entry(root, width=20, bd=5, font=('Times', 20), justify='right', bg='gray67')
display.pack(pady=5)

#Frame for button
btn_frame= tk.Frame(root, bg='gray25')
btn_frame.pack(padx=10, pady=10)

#2D list of calculator button
buttons= [['C','(',')','/'],
          ['7','8','9','*'],
          ['4','5','6','-'],
          ['1','2','3','+'],
          ['.','0','%','='],
          ['ans']]


#clickable button function
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        if i == 0 or j == 3:   #colour for buttons boarder and text
            bg_colour = 'cornsilk3'
            fg_colour = 'black'
        else:
            fg_colour = 'black'
            bg_colour = 'white'
        button = tk.Button(btn_frame, text=buttons[i][j], font=('Times', 16), width = 3, height=1, bg=bg_colour, fg=fg_colour)
        button.grid(row=i, column=j, padx=10, pady=10)
        button.bind('<Button-1>', click)


#keeps calculator window active and responsive
root.mainloop()



