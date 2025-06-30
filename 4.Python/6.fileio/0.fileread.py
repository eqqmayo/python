file_path = 'file.txt'
file = open(file_path, 'r') # file 을 file descriptor 라고 부름 FD

file.write('blahblah')

file.close()