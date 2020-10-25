import pdfkit

options = {
    "enable-local-file-access": None,
    "page-size": "A5",
    "viewport-size": "1366 x 768",
    'disable-smart-shrinking': '',
    'margin-top': '0in',
    'dpi': 900,
    'margin-right': '0.8in',
    'margin-bottom': '0in',
    'margin-left': '0.8in',
}

pdfkit.from_file("D:\Misc Practice\Chatbot\Rasa Projects\webpages\page2.html", './staticpdfs/myfile.pdf', options=options)
