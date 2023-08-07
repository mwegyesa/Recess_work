import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
import uuid


class ReceiptGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt Generator")
        self.geometry("400x500")

        self.receipt_number = str(uuid.uuid4())[:8]
        self.customer_name = ""
        self.customer_address = ""
        self.items = []
        self.total_amount = 0.0

        self.create_widgets()

    def create_widgets(self):
        self.customer_name_label = tk.Label(self, text="Customer Name:")
        self.customer_name_label.pack()
        self.customer_name_entry = tk.Entry(self)
        self.customer_name_entry.pack()

        self.customer_address_label = tk.Label(self, text="Customer Address:")
        self.customer_address_label.pack()
        self.customer_address_entry = tk.Entry(self)
        self.customer_address_entry.pack()

        self.item_name_label = tk.Label(self, text="Item Name:")
        self.item_name_label.pack()
        self.item_name_entry = tk.Entry(self)
        self.item_name_entry.pack()

        self.item_price_label = tk.Label(self, text="Item Price:")
        self.item_price_label.pack()
        self.item_price_entry = tk.Entry(self)
        self.item_price_entry.pack()

        self.add_item_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_item_button.pack()

        self.item_listbox = tk.Listbox(self)
        self.item_listbox.pack()

        self.generate_receipt_button = tk.Button(
            self, text="Generate Receipt", command=self.generate_receipt
        )
        self.generate_receipt_button.pack()

    def add_item(self):
        item_name = self.item_name_entry.get()
        item_price = float(self.item_price_entry.get())

        self.items.append((item_name, item_price))
        self.item_listbox.insert(tk.END, f"{item_name}: ${item_price:.2f}")

        self.item_name_entry.delete(0, tk.END)
        self.item_price_entry.delete(0, tk.END)

    def generate_receipt(self):
        self.customer_name = self.customer_name_entry.get()
        self.customer_address = self.customer_address_entry.get()

        receipt = [
            ["----- MS ENTERPRISE LTD -----"],
            ["Receipt Number:", self.receipt_number],
            ["Customer Name:", self.customer_name],
            ["Address:", self.customer_address],
            [],  # Empty row
            ["Item", "Price"],
        ]

        for item_name, item_price in self.items:
            receipt.append([item_name, f"${item_price:.2f}"])

        receipt.append([])  # Empty row
        receipt.append(["Total Amount:", f"${self.calculate_total():.2f}"])
        receipt.append(["--------------------------------"])
        receipt.append(["Thank you for your purchase!"])

        messagebox.showinfo("Receipt", self.format_receipt(receipt))
        self.create_pdf(receipt)

    def format_receipt(self, receipt):
        formatted_receipt = ""
        for row in receipt:
            formatted_row = " ".join(str(cell) for cell in row)
            formatted_receipt += formatted_row + "\n"
        return formatted_receipt

    def calculate_total(self):
        self.total_amount = sum(item[1] for item in self.items)
        return self.total_amount

    def create_pdf(self, receipt):
        pdf_filename = f"receipt_{self.receipt_number}.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)

        x_margin = 50
        y_margin = 700
        line_height = 20

        # Set font and font size for the receipt
        c.setFont("Helvetica", 12)

        # Draw receipt header
        c.drawString(x_margin, y_margin, "----- MS ENTERPRISE LTD -----")
        y_margin -= line_height

        # Draw receipt details
        c.drawString(x_margin, y_margin, "Receipt Number:")
        c.drawString(x_margin + 120, y_margin, self.receipt_number)
        y_margin -= line_height

        c.drawString(x_margin, y_margin, "Customer Name:")
        c.drawString(x_margin + 120, y_margin, self.customer_name)
        y_margin -= line_height

        c.drawString(x_margin, y_margin, "Address:")
        c.drawString(x_margin + 120, y_margin, self.customer_address)
        y_margin -= line_height * 6

        

        # Draw item table
        item_table = Table(receipt[5:-3])
        item_table.setStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"), ("VALIGN", (0, 0), (-1, -1), "TOP")])
        item_table.wrapOn(c, 300, 500)
        item_table.drawOn(c, x_margin, y_margin)


        c.drawString(x_margin, y_margin, "-----------------************---------------")

        # Draw total amount and footer
        y_margin -= line_height * (len(receipt) - 7)
        c.drawString(x_margin, y_margin, "Total Amount:")
        c.drawString(x_margin + 120, y_margin, f"${self.calculate_total():.2f}")
        y_margin -= line_height

        c.drawString(x_margin, y_margin, "--------------------------------")
        y_margin -= line_height

        c.drawString(x_margin, y_margin, "Thank you for your purchase!")
        y_margin -= line_height

        # Save the PDF file
        c.save()
        messagebox.showinfo("PDF Generated", f"PDF receipt saved as {pdf_filename}")


if __name__ == "__main__":
    app = ReceiptGenerator()
    app.mainloop()
