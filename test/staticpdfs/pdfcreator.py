import pdfkit
from pyrebase import pyrebase

options = {
    "enable-local-file-access": None,
    "page-size": "A5",
    "viewport-size": "1366 x 768",
    'disable-smart-shrinking': '',
    'margin-top': '0in',
    'dpi': 900,
    'margin-right': '0.27in',
    'margin-bottom': '0in',
    'margin-left': '0.27in',
}

# pdfkit.from_file("source_html_path","dest_pdf_path",options = options)

# pdfkit.from_file("C:/Users/Saumitra/Desktop/page1.html", 'heartbreak.pdf', options=options)



###-------------IGNORE THESE-----------------------------------------###
config = {
    "apiKey": "AIzaSyB7cTfNmxp_OA9vOKL94O10FRHe_PyyziQ",
    "authDomain": "whoabot-181f2.firebaseapp.com",
    "databaseURL": "https://whoabot-181f2.firebaseio.com",
    "projectId": "whoabot-181f2",
    "storageBucket": "whoabot-181f2.appspot.com",
    "messagingSenderId": "437598146366",
    "appId": "1:437598146366:web:b36b6702a749b7466da66f",
    "measurementId": "G-LCRZ7MP631"
}
def upload_pdf():
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    path_local = "./Heartbreak/1.pdf"
    path_on_cloud = "pdfs/Heartbreak/heartbreak.pdf"
    storage.child(path_on_cloud).put(path_local)
    print(storage.child(path_on_cloud).get_url(path_on_cloud))

def get_pdf(story,number):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    path_on_cloud = "pdfs/{}/{}.pdf".format(str(story),str(number))
    print(storage.child(path_on_cloud).get_url(path_on_cloud))
    return storage.child(path_on_cloud).get_url(path_on_cloud)

# if __name__ == "__main__":
#     get_pdf("Anxiety","anxiety1-1")

