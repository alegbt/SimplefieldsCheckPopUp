import tkinter as tk
from tkinter.font import Font


def create_popup():
    popup = tk.Toplevel()  # Create a new top-level window
    popup.title("Resizable Popup")
    popup.geometry("500x500")  # Initial size of the popup

    # Custom fonts
    bold_font = Font(family="Helvetica", size=21, weight="bold")
    normal_font = Font(family="Helvetica", size=19)
    input_font = Font(family="Helvetica", size=18)

    # Function to reset all fields
    def reset_fields():
        input_field.delete(0, tk.END)
        for cb_var in checkbutton_vars:
            cb_var.set(0)

    # Input field at the top
    input_field = tk.Entry(popup, font=input_font)
    input_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    # Reset button
    reset_btn = tk.Button(popup, text="Reset", font=normal_font, command=reset_fields)
    reset_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    # Content
    labels = ["DOCUMENTO ID", "Numero Documento id", "Data rilascio documento id",
              "Scadenza documento id", "TESSERA SANITARIA", "Scadenza tessera Sanitaria", "Codice fiscale"]

    checkbutton_vars = []  # Keep track of the checkbutton variables

    for i, text in enumerate(labels):
        if text in ["DOCUMENTO ID", "TESSERA SANITARIA"]:
            label = tk.Label(popup, text=text, font=bold_font)
        else:
            label = tk.Label(popup, text=text, font=normal_font)
        label.grid(row=i + 2, column=0, sticky='w', pady=2, padx=10)

        cb_var = tk.IntVar()  # Variable to track the checkbutton state
        checkbutton = tk.Checkbutton(popup, variable=cb_var)
        checkbutton.grid(row=i + 2, column=1, sticky='w')
        checkbutton_vars.append(cb_var)  # Add to list for tracking

    popup.resizable(True, True)  # Make the popup resizable


# Create the main application window
root = tk.Tk()
root.title("Main Window")

# Button to open the popup
open_popup_btn = tk.Button(root, text="Open Popup", command=create_popup)
open_popup_btn.pack(pady=20)

# Start the application
root.mainloop()
