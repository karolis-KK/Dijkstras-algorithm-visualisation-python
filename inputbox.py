import customtkinter as ctk

# window
app = ctk.CTk()
app.geometry("325x250")
app.title("Input")

app.grid_columnconfigure((0), weight=1)

entry_start_x = ctk.CTkEntry(app, placeholder_text="Start X")
entry_start_x.grid(row=0, column=0, padx=10, pady=(20, 20), sticky="ew")

entry_start_y = ctk.CTkEntry(app, placeholder_text="Start Y")
entry_start_y.grid(row=0, column=1, padx=10, pady=(20, 20), sticky="ew")

entry_end_x = ctk.CTkEntry(app, placeholder_text="End X")
entry_end_x.grid(row=1, column=0, padx=10, pady=(20, 20), sticky="ew")

entry_end_y = ctk.CTkEntry(app, placeholder_text="End Y")
entry_end_y.grid(row=1, column=1, padx=10, pady=(20, 20), sticky="ew")

def button_event():
    start_x = entry_start_x.get()
    start_y = entry_start_y.get()
    end_x = entry_end_x.get()
    end_y = entry_end_y.get()

    print(f"Start X: {start_x}")
    print(f"Start Y: {start_y}")
    print(f"End X: {end_x}")
    print(f"End Y: {end_y}")

button = ctk.CTkButton(app, text="Enter", command=button_event)
button.place(relx=0.5, rely=0.8, anchor='center')

def checkbox_event():
    print(check_var.get())

check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(app, text="Show search", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox.place(relx=0.5, rely=0.6, anchor='center')

# loop
app.mainloop()
