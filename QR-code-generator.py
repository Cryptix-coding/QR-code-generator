import tkinter as tk
from tkinter import messagebox
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x370")

        # Padding values for cleaner layout
        self.pad_y = 5

        # Center column 0
        self.root.grid_columnconfigure(0, weight=1)

        # Create and place UI elements
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Text or URL for the QR Code:").grid(row=0, column=0, pady=(15, 0))
        self.data_entry = tk.Entry(self.root, width=40)  # Increased width for larger input field
        self.data_entry.grid(row=1, column=0, pady=self.pad_y)

        tk.Label(self.root, text="QR Code size (e.g., 10):").grid(row=2, column=0, pady=self.pad_y)
        self.size_entry = tk.Entry(self.root, width=40)  # Increased width for larger input field
        self.size_entry.insert(0, "10") # Default value
        self.size_entry.grid(row=3, column=0, pady=self.pad_y)

        tk.Label(self.root, text="Border width (e.g., 4):").grid(row=4, column=0, pady=self.pad_y)
        self.border_entry = tk.Entry(self.root, width=40)  # Increased width for larger input field
        self.border_entry.insert(0, "4") # Default value
        self.border_entry.grid(row=5, column=0, pady=self.pad_y)

        tk.Label(self.root, text="Filename (without .png):").grid(row=6, column=0, pady=self.pad_y)
        self.name_entry = tk.Entry(self.root, width=40)  # Increased width for larger input field
        self.name_entry.grid(row=7, column=0, pady=self.pad_y)

        # Button to generate QR code
        generate_btn = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        generate_btn.grid(row=8, column=0, pady=20)
        generate_btn.bind("<Return>", self.generate_qr) # Allow generation via Enter key

        tk.Label(self.root, text="The image will be saved in the same folder.", font=("Arial", 8, "italic")).grid(row=9, column=0)

    def generate_qr(self, event=None):
        # Retrieve user inputs
        text_data = self.data_entry.get()
        filename = self.name_entry.get()

        # Check if text and filename are not empty
        if not text_data or not filename:
            messagebox.showwarning("Input Error", "Please fill in at least the text and filename fields.")
            return

        try:
            # Try to convert size and border inputs to integers
            # If fields are empty, use default values (e.g., 10 and 4)
            box_size_val = int(self.size_entry.get()) if self.size_entry.get() else 10
            border_val = int(self.border_entry.get()) if self.border_entry.get() else 4

            # Generate QR code
            qr = qrcode.QRCode(box_size=box_size_val, border=border_val)
            qr.add_data(text_data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image (append .png if the user forgot it)
            if not filename.endswith(".png"):
                filename += ".png"

            img.save(filename)

            # Success message for the user
            messagebox.showinfo("Success!", f"The QR code was successfully saved as '{filename}'.")

        except ValueError:
            # If the user enters text in numeric fields
            messagebox.showerror("Error", "Please enter only whole numbers for 'Size' and 'Border'.")
        except Exception as e:
            # Catch all other unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()