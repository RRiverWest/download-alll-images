import img2pdf
import glob
from natsort import natsorted

# PDf化させたい画像を一括で取得
lists = list(glob.glob("./images/*"))

# PDFファイル出力
pdfpath = "output.pdf"
with open(pdfpath, "wb") as f:
    f.write(img2pdf.convert([str(i) for i in natsorted(lists) if ".jpg" in i]))
