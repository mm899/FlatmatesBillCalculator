import webbrowser
import os

from fpdf import FPDF
from filestack import Client


class PdfReport:

    """
    Creates a PDF file that contains data about the flatmates such as their names,
    their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title and logo
        pdf.image('files/house.png', w=40)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')  # Changing font size
        pdf.cell(w=115, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0)
        pdf.cell(w=115, h=40, txt='Total bill amount:', border=0)
        pdf.cell(w=0, h=40, txt='£' + str(bill.amount), border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)  # Changing font size and style
        pdf.cell(w=0, h=40, txt='Each flatmate to pay:', border=0, ln=1)
        pdf.set_font(family='Times', size=10)  # Changing font size and style
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=0, h=40, txt='£ ' + str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2)), border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=0, h=40, txt='£ ' + str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)), border=0, ln=1)

        pdf.output('files/' + self.filename)  # Saves the PDF output file into the 'files' directory

        os.chdir('files')  # Changes the directory sp that the web browser can open the PDF file
        webbrowser.open(self.filename)


class FileSharer:

    """
    Shares files to file stacker servers and shares the public URL.
    """

    def __init__(self, filepath, api_key=''):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url
