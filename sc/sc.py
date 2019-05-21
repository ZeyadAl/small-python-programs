import os
a = "wget https://people.eecs.berkeley.edu/~bh/pdf/ssch"
c= ".pdf"

for i in range(28):
    n = '{num:02d}'.format(num=i)
    b = a + n + c
    os.system(b)

os.system('PDFjoin -o s.pdf *.pdf')
#rm could be dangorous. Maybe should specify more
os.system('rm ss*')

