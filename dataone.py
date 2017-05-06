import csv

inputdata = input()
inputdata = inputdata.split(' ')
shopid = shopno = "0"
price = 0.00
a=[0]*len(inputdata)
m=100.00
flag=1
f=0

with open('./'+inputdata[0]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if f==0:
            f=1
            continue
        row[2] = row[2].split(',')
        row[2] = [i.strip() for i in row[2]]
        if flag==1:
            for j in range(1, len(inputdata)):
                if a[j] == 1:
                    flag=0
                else:
                    flag=1
                    break
        if shopno!=row[0]:
            for q in range(len(a)):
                a[q] = 0
        for j in range(1, len(inputdata)):
            if a[j]==1:
                continue
            for i in row[2]:
                if i == inputdata[j]:
                    if shopno!=row[0]:
                        for q in range(len(a)):
                            a[q]=0
                        shopno = row[0]
                        price = 0
                    price+=float(row[1])
                    a[j]=1
        for j in range(1,len(a)):
            if a[j]!=1:
                s=1
                break
            s=0
        if s==0:
            if m>price:
                m=price
                shopid=shopno
    if flag==1:
        print("none")
        quit()
    print(shopid,m)