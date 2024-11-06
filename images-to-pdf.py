import img2pdf
import glob
from natsort import natsorted

lists = list(glob.glob("./images/*"))
pdfpath = "output.pdf"
with open(pdfpath, "wb") as f:
    f.write(img2pdf.convert([str(i) for i in natsorted(lists) if ".jpg" in i]))
