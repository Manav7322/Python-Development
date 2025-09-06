from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

company = "Apple"
symbol = "AAPL"
price = 187.65
change = "+1.24%"

text = f"{company} stock ({symbol}) closed at ${price} today ({change})."

data = [
    ["Date", "Open", "High", "Low", "Close"],
    ["2025-09-01", 185.0, 188.2, 184.5, 187.65],
    ["2025-09-02", 187.2, 190.0, 186.0, 188.5]
]

c = canvas.Canvas("simple.pdf", pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 20)
c.drawString(100, 750, "Stock Report")

# Body text
c.setFont("Helvetica", 12)
c.drawString(100, 720, text)

x = 100
y = 680
for row in data:
    c.drawString(x, y, "   ".join(map(str, row)))
    y -= 20

c.save()
