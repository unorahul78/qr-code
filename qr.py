import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Entry widget for user input
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to generate QR code
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.grid(row=0, column=1, padx=10, pady=10)

        # Button to download QR code
        self.download_button = tk.Button(root, text="Download QR Code", command=self.download_qr_code, state=tk.DISABLED)
        self.download_button.grid(row=0, column=2, padx=10, pady=10)

        # Canvas to display QR code
        self.qr_canvas = tk.Canvas(root, width=300, height=300)
        self.qr_canvas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Initialize qr_img_pil attribute
        self.qr_img_pil = None

    def generate_qr_code(self):
        # Get user input from entry widget
        text = self.text_entry.get().strip()

        if text:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            # Create PIL image from QR code instance
            self.qr_img_pil = qr.make_image(fill='black', back_color='white')

            # Convert PIL image to Tkinter PhotoImage
            self.qr_tk_img = ImageTk.PhotoImage(self.qr_img_pil)

            # Display QR code on canvas
            self.qr_canvas.delete("all")
            self.qr_canvas.create_image(0, 0, anchor="nw", image=self.qr_tk_img)

            # Enable download button
            self.download_button.config(state=tk.NORMAL)

        else:
            messagebox.showerror("Error", "Please enter text to generate QR code.")

    def download_qr_code(self):
        # Get file path for saving the QR code image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

        if file_path and self.qr_img_pil:
            try:
                # Save the QR code image
                self.qr_img_pil.save(file_path)
                messagebox.showinfo("Success", "QR code saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
