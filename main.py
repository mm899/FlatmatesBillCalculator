from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

# getting the user inputs
bill_amount_input = float(input('Hey user, enter the bill amount: '))
bill_period_input = input('Please enter the bill period (Month, Year): ')

flatmate1_name_input = input('Please enter the first flatmates name: ')
flatmate2_name_input = input('Please enter the second flatmates name: ')

flatmate1_days_input = int(input(f'Please enter the number of days {flatmate1_name_input} has spent in the house '
                                 f'during the period: '))
flatmate2_days_input = int(input(f'Please enter the number of days {flatmate2_name_input} has spent in the house '
                                 f'during the period: '))

the_bill = Bill(amount=bill_amount_input, period=bill_period_input)
flatmate1Obj = Flatmate(name=flatmate1_name_input, days_in_house=flatmate1_days_input)
flatmate2Obj = Flatmate(name=flatmate2_name_input, days_in_house=flatmate2_days_input)

print(flatmate1Obj.name + " pays: £" + str(flatmate1Obj.pays(bill=the_bill, flatmate2=flatmate2Obj)))
print(flatmate2Obj.name + " pays: £" + str(flatmate2Obj.pays(bill=the_bill, flatmate2=flatmate1Obj)))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1=flatmate1Obj, flatmate2=flatmate2Obj, bill=the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
