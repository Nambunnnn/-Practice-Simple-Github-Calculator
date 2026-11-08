import customtkinter as tk

root = tk.CTk()
root.geometry("490x340")
root.title("เครื่องคิดเลข")

expression = ""
field = tk.CTkEntry( root, height=60,font=("Times New Roman", 25), corner_radius=15,)
field.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="ew")


def update_display():
    field.delete(0, "end")
    field.insert(0, expression)
def add_to_display(value):
    global expression
    expression += str(value)
    update_display()
def clear_display():
    global expression
    expression = ""
    update_display()
def calculate():
    global expression
    try:
        result = str(eval(expression))
        expression = result
        update_display()
    except ZeroDivisionError:
        expression = ""
        field.delete(0, "end")
        field.insert(0, "Cannot divide by zero")
    except Exception:
        expression = ""
        field.delete(0, "end")
        field.insert(0, "Error")
def create_button(text_value, command, row, column):
    button = tk.CTkButton(root,text=text_value,width=90,height=55,corner_radius=12,font=("Times New Roman", 20),command=command, )
    button.grid(row=row, column=column, padx=4, pady=4)
# Number buttons
for number in range(1, 10):
    row = (number - 1) // 3 + 1
    column = (number - 1) % 3
    create_button(str(number), lambda value=number: add_to_display(value), row, column)

create_button("0", lambda: add_to_display(0), 4, 1)
create_button("+", lambda: add_to_display("+"), 1, 3)
create_button("-", lambda: add_to_display("-"), 2, 3)
create_button("*", lambda: add_to_display("*"), 3, 3)
create_button("/", lambda: add_to_display("/"), 4, 3)
create_button("^", lambda: add_to_display("**"), 4, 4)
create_button("(", lambda: add_to_display("("), 1, 4)
create_button(")", lambda: add_to_display(")"), 2, 4)
create_button(".", lambda: add_to_display("."), 3, 4)
create_button("=", calculate, 4, 2)
create_button("C", clear_display, 4, 0)

root.mainloop()