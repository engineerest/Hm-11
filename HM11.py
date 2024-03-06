# буду писать на русском потому что удобно(коментарии)
import os
import random
import time
from ContentData import massiveRndm, result
class file:
    def __init__(self, fileName, fileContent, fileCreateTime, filePath, fileSize): # Создание имени файла, контент и тд
        self.fileName = fileName
        self.fileContent = fileContent
        self.fileCreateTime = fileCreateTime
        self.filePath = filePath
        self.fileSize = fileSize

    @staticmethod
    def generateFile(cls, nameFile):
        GEN_FOLDER = 'generalFolder' # Название
        if not os.path.exists(GEN_FOLDER):
            os.mkdir(GEN_FOLDER)  # Создание главной папки

        count = random.randint(1, 11) # генерация количеста файлов

        files = [] # Лист для данных
        for i in range(count):
            fileName = f"{nameFile}_{i}.txt" # Название файла
            file_path = os.path.join(GEN_FOLDER, fileName) # Путь

            with open(file_path, "w+") as f: # Записать вот эти Научные исследования и Твір
                f.write(result)
            fileCreateTime = time.ctime() # Когда был создан файл
            fileSize = os.path.getsize(file_path) # Размер файла
            files.append(cls(fileName, result, fileCreateTime, file_path, fileSize)) # Добавить данные файла в лист
        return files # Вернуть лист для дальнейшого использывания

    @staticmethod
    def listFiles(folderPath): # Функция для вывода файлов списком
        try:
            files = os.listdir(folderPath)
            return files
        except FileNotFoundError:
            print(f"Папка {folderPath} не знайдена")

    @classmethod
    def initializeObjects(cls, nameFile): #  Инцилизация с классметодом
        files = cls.generateFile(cls, nameFile) # Зайти в генерейт файл для общего вывоа
        return files

nameFile = input("Як назвати файл в папці?: ")
fileInitObj = file.initializeObjects(nameFile)
fileListOutput = file.listFiles('generalFolder')
print(f"\n{fileListOutput}\n") # Вывод файлов ввиде списка
for o in fileInitObj: # Вывод инцилизации
    print(f"Назва файлу: {o.fileName}")
    print(f"Контент: {o.fileContent}")
    print(f"Час створення: {o.fileCreateTime}")
    print(f"Повний шлях: {o.filePath}")
    print(f"Розмір файлу: {o.fileSize} байт\n")


# Некоторые комманды взяты с интернета, прошу не судить строго