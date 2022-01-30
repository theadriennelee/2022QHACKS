from transcriber import transcriber
from pdfmake import pdf
import shutil

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')

original=r"C:\Users\Admin\Downloads\trimmed.mp4"
target=r"C:\Users\Admin\Downloads\c0.mp4"
target1=r"C:\Users\Admin\Downloads\c1.mp4"

shutil.copyfile(original, target)
shutil.copyfile(original, target1)

a = transcriber(r"C:\Users\Admin\Downloads\trimmed.mp4")
print(a)
a.wait()
foo = a.getparagraphs()
start,end = a.gettstamps()

pdf = pdf("test1", foo,start,end,r"C:\Users\Admin\Downloads\tcopy.mp4")
pdf.gen2()



