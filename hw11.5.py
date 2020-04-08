filename = input("입력 파일 이름 : ")
infile = open(filename, "r")
rfile = infile.readlines()
infile.close()

a = 0
n= 0
total = 0
aver = 0

for a in rfile:
    total += float(a)
    n +=1

aver = total / n

print(total)
print(aver)

outfile = open("output.txt", "w")
outfile.write(str(total))
outfile.write("\n")
outfile.write(str(aver))

outfile.close()
