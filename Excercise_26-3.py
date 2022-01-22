# ฝึกการใช้ List comprehension โดยการเลือกตัวเลขที่ซ้ำกันระหว่าง File 1 และ File 2ห

with open("./file1.txt") as file1:
    data_1 = file1.readlines()

with open("./file2.txt") as file2:
    data_2 = file2.readlines()

result = [int(n) for n in data_1 if n in data_2]

print(result)


