from fpdf import FPDF


class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.generate()

    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        return cls(name)

    def generate(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font("Helvetica", "B", 50)
        pdf.cell(
            0, 50, txt="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT"
        )

        pdf.image("shirtificate.png", x=5, y=80, w=200)

        pdf.set_font("Helvetica", "B", size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 180, align="C", txt=f"{self.name} took CS50")

        pdf.output("shirtificate.pdf")


def main():
    Shirtificate.get()


if __name__ == "__main__":
    main()



"""
from fpdf import FPDF
class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self.text(0, 0, text="CS50 Shirtificate")
        self._pdf.ln(h=20)
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self.text(-250, 255, text=f"{name} took CS50")

    # def footer(self):
    #     # Position cursor at 1.5 cm from bottom:
    #     self.set_y(-15)
    #     # Setting font: helvetica italic 8
    #     self.set_font("helvetica", "I", 8)
    #     # Printing page number:
    #     self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
    def text(self, heights, colour, text):
        self._pdf.set_text_color(r=int(colour))
        self._pdf.set_font("Times", size=36)
        self._pdf.cell(
            w=0, h=heights, txt=text, new_x="LMARGIN", new_y="NEXT", align="C"
        )
    def out(self,shirt):
        self._pdf.output(shirt)


# Instantiation of inherited class
# pdf = PDF()
# pdf.add_page()
# pdf.set_font("Times", size=12)
# pdf.output("new-tuto2.pdf")
string = input("Name: ")
string = PDF(string)
string.out("shirtificate.pdf")

"""