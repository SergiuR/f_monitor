import os
from datetime import datetime
import time

#Создание проверка наличия папки log
#В случае её отсутствия создаётся новая 
if os.path.exists("log") == False: 
	os.mkdir("log")

#Создание лог файла в папке log
#В качестве имени файла используется дата и время создания
log_file_name = datetime.strftime(datetime.now(), "%Y.%m.%d-%H.%M.%S")
log_file = r"log\%s.txt" %log_file_name
new_log_file = open(log_file, "w")
new_log_file.close()

#Запись в лог файл имен файлов и папок обнаруженых при запуске скрипта
path = r"C:\projects\daemon\tmp"
first_write = open(log_file, "a")
first_write.write("Файлы обнаруженные при запуске: \n" + ("-" * 48) + "\n")
for root, dirs, files in os.walk(path):
	for item in dirs:
		first_write.write("DIR    " + path + "\\" + item + "\n")
	for item in files:
		first_write.write("FILE   " + path + "\\" + item + "\n")

first_write.write(("-" * 48) + ("\n" * 2))
first_write.close()

while True:
	write_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H.%M.%S")
	write_log = open(log_file, "a")
	write_log.write("Снимок сделан: " + write_time + "\n" + ("-" * 48) + "\n")
	for root, dirs, files in os.walk(path):
		for item in dirs:
			write_log.write("DIR    " + item + "\n")
		for item in files:
			write_log.write("FILE   " + item + "\n")
	write_log.write("-" * 48 + "\n" * 2)
	write_log.close()
	time.sleep(10)
