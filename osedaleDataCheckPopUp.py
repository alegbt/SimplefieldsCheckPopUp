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


    # Input field at the top
    input_field = tk.Entry(popup, font=input_font)
    input_field.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    # Content
    labels = ["DOCUMENTO ID",
              "Numero Documento id",
              "Data rilascio documento id",
              "Scadenza documento id",
              "TESSERA SANITARIA",
              "Scadenza tessera Sanitaria",
              "Codice fiscale"]

    for i, text in enumerate(labels):
        if text in ["DOCUMENTO ID", "TESSERA SANITARIA"]:
            label = tk.Label(popup, text=text, font=bold_font)
        else:
            label = tk.Label(popup, text=text, font=normal_font)
        label.grid(row=i+1, column=0, sticky='w', pady=2, padx=10)

        # Checkbutton with increased font size
        checkbutton = tk.Checkbutton(popup)
        checkbutton.grid(row=i+1, column=1, sticky='w')

    popup.resizable(True, True)  # Make the popup resizable

# Create the main application window
root = tk.Tk()
root.title("Main Window")

# Button to open the popup
open_popup_btn = tk.Button(root, text="Open Popup", command=create_popup)
open_popup_btn.pack(pady=20)

# Start the application
root.mainloop()
