import pdfkit

html = """
<h1>Stock Report</h1>
<p>Apple Stock (AAPL) closed at $187.65 today (+1.24%).</p>
"""

pdfkit.from_string(html, "output.pdf")