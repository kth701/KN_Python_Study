#문자열(string)=> indexing , slicing
str1 = "python"
str2 = "01234"

print(str1, str2)
print(str1[0], str1[1], str1[2], str1[3], str1[4], str1[5])
print(str1[-1], str1[-2], str1[-3], str1[-4], str1[-5], str1[-6])

print(str2[0], str2[1], str2[2], str2[3], str2[4])
print(str2[-1], str2[-2], str2[-3], str2[-4], str2[-5])

# 문자열 연산(+) => 문자열연결
print("python" + "," + " program")
print("python"+str(3.13)+"=>"+str(100*3))
