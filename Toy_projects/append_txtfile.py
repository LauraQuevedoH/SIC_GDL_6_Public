f = open("test.txt", 'a')
for i in range(9,11):
	data = f"Line {i}!\n"
	f.write(data)

f.close()
