s = input("Nhập chuỗi của bạn: ")
words = [tu for tu in s.split(" ")]
print (" ".join(sorted(list(set(words)))))