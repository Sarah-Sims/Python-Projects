from fpdf import FPDF

def main():

    #, implement a program that prompts the user for their name and outputs,
    create_shirt(input("Name: "))

    #TO DO

def create_shirt(user_name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
   # pdf.set_font_color(255, 255, 0)
    pdf.set_auto_page_break(0)
    pdf.cell(200, 10, txt="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.multi_cell(200, 300, txt=text(user_name ), align='C')
    pdf.output("shirtificate.pdf")

def text(user_name):
    user_CS50 = user_name + " took CS50"
    return user_CS50

if __name__ == "__main__":
    main()