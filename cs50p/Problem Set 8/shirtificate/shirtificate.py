from fpdf import FPDF

name = input('Name: ')

pdf = FPDF()
pdf.add_page()
pdf.set_y(20)
pdf.set_font('Helvetica', 'B', 30)
pdf.cell(text='CS50 Shirtificate', align='C', center='True')
pdf.set_y(50)
pdf.image('shirtificate.png', x=0)
pdf.set_y(120)
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(255,255,255)
pdf.cell(text=f'{name} took CS50', align='C', center='True')
pdf.output('shirtificate.pdf')
