from fpdf import FPDF
import inflect

# Function to convert numbers to words in Indian currency
def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number)
    words = words.replace(',', '')  # Remove commas from the words
    words = words.replace(' and', '')  # Remove 'and' from the end
    words = words.replace('-', ' ')  # Replace hyphens with spaces
    words = words.title()  # Capitalize the first letters
    words += " Indian Rupees Only"
    return words

# Function to create a payment receipt
def create_receipt(customer_name, amount, discount, gst):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Payment Receipt", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(100, 10, f"Customer: {customer_name}", ln=True)
    pdf.cell(100, 10, f"Amount: INR {amount:.2f}", ln=True)
    pdf.cell(100, 10, f"Discount: INR {discount:.2f}", ln=True)
    pdf.cell(100, 10, f"GST: INR {gst:.2f}", ln=True)
    
    total_amount = amount - discount + gst
    pdf.cell(100, 10, f"Total Amount: INR {total_amount:.2f}", ln=True)
    
    amount_in_words = convert_to_words(total_amount)
    pdf.cell(200, 10, f"Total Amount in Words: {amount_in_words}", ln=True)
    
    pdf.output("payment_receipt.pdf")

# Input values
customer_name = "John Doe"
amount = 1000
discount = 100
gst = 18

create_receipt(customer_name, amount, discount, gst)
