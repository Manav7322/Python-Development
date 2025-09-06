from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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

pdf = SimpleDocTemplate("stock Price.pdf", pagesize = letter)
styles = getSampleStyleSheet()

elements = []

elements.append(Paragraph("Stock Report", styles["Title"]))

elements.append(Paragraph(text, styles["Normal"]))
# elements.append(Spacer(1,12))

#Table
table = Table(data)
elements.append(table)

pdf.build(elements)