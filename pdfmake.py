from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import vidcap as vc
import cv2

class pdf:

    doc = []

    def __init__(self,title, listofp,start,end, path):
        self.title = title
        self.listofp = listofp
        self.start = start
        self.end = end
        self.canvas = canvas.Canvas(title + '.pdf', pagesize=letter)
        self.video = path

    def gen2(self):
        self.addTitle()
        for n in range(len(self.listofp)):
            self.addParagraph(self.listofp[n])
            cwd = vc.getframe(self.video,self.start[n])
            self.addImage(cwd)
        SimpleDocTemplate('pic.pdf', pagesize=letter, rightMargin=12, leftMargin=12, topMargin=12,
                          bottomMargin=6).build(self.doc)


    def addTitle(self):
        self.doc.append(Spacer(1, 20))
        self.doc.append(Paragraph(self.title,
                             ParagraphStyle(name="Title", fontFamily='Helvetica', fontSize=32, alignment=TA_LEFT)))
        self.doc.append(Spacer(1, 50))


    def addParagraph(self,line):
        self.doc.append(Paragraph(line))
        self.doc.append(Spacer(1, 20))

    def addImage(self, image):
        self.doc.append(Spacer(1, 20))
        self.doc.append(Image(image, 4 * inch, 2.2 * inch))
        self.doc.append(Spacer(1, 50))





