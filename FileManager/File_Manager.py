import os
import shutil
from tabulate import tabulate
from distutils.dir_util import copy_tree


class FileManager:
    def __init__(self):
        self.root_directory = "/home/noble6/File_manager_directory/"
        self.directory_data = []
        self.run_state = False

    def create_directory(self):
        directory_name = str(input("Directory name: "))
        # Path(self.root_directory).mkdir(parents=True, exist_ok=True)
        if not os.path.exists(f'{self.root_directory}/{directory_name}'):
            os.makedirs(f'{self.root_directory}/{directory_name}')
        else:
            print("Directory already exists")

    def create_file(self):
        file_name = str(input("File name: "))
        new_file = open(f"{self.root_directory}/{file_name}", "w")
        new_file.write(str(input()))
        new_file.close()

    def read_file(self):
        try:
            file_location = f"{self.root_directory}/{str(input('Введите название файла чтобы прочитать: '))}"
            with open(f"{file_location}.txt", "r") as f:
                text = f.readlines()
                print(text)
        except FileNotFoundError:
            print("Файл не найден")

    def list_directory(self):
        files = os.scandir(path=self.root_directory)
        file_id = 1
        for each in files:
            object_data = f' - Directory - {each.name} - {file_id}' if each.is_dir() else f' - File - {each.name} - {file_id}'
            object_info = object_data.split(' - ')
            object_info.pop(0)
            self.directory_data.append(object_info)
            file_id += 1
        data = tabulate((i for i in self.directory_data), headers=['Type', 'Name', 'ID'], tablefmt='pipe', stralign='center')
        self.directory_data = []
        print(data)

    def list_stats(self):
        files = os.scandir(path=self.root_directory)
        for each in files:
            print(os.stat(each))

    def delete_directory(self):
        directory = str(input('Directory to delete: '))
        try:
            os.rmdir(f'{self.root_directory}/{directory}')
        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')

    def move_between_directories(self):  # Переместиться по директориям
        directories = os.scandir(path=self.root_directory)
        for each in directories:
            if each.is_dir():
                print(f'- Directory - {each.name}')
        choosen_directory = str(input('Type Directory Name: '))
        self.root_directory += f'{choosen_directory}'

    def move_up(self):  # Подняться вверх по директории
        location = self.root_directory.split('/')
        location.pop()
        up = '/'.join(location)
        self.root_directory = up

    def rename_file(self):
        print('Список файлов и директорий для переименовывания: ')
        self.list_directory()
        file_to_rename = f"{self.root_directory}/{str(input('Введите название файла, чтобы переименовать: '))}"
        new_name = str(input('Введите новое название файла: '))
        os.rename(file_to_rename, f'{self.root_directory}/{new_name}')

    def copy_files(self):
        self.list_directory()
        start_directory = f"{self.root_directory}/{str(input('Директория из который производится копирование: '))}"
        end_directory = f"{self.root_directory}/{str(input('Название новой директории, чтобы скопировать в неё: '))}"
        copy_tree(start_directory, end_directory)

    def move_files(self):
        self.list_directory()
        # start_directory = f"{self.root_directory}/{str(input('Файл для перемещения: '))}"
        # end_directory = f"{self.root_directory}/{str(input('П: '))}"

    def CLI(self):
        print('Файловый менеджер\n')
        commands = [['1', 'Просмотр директории'], ['2', 'Создать папку']]
        help_page = tabulate((i for i in commands), headers=['ID', 'Метод'], tablefmt='grid', stralign='center')
        print(help_page)
        while True:
            choose = str(input('\nВведите ID команды чтобы продолжить: '))
            print('\n')
            if choose == '1':
                self.list_directory()
            if choose == 'help':
                print(f'\n{help_page}')
            if choose.lower() == 'exit':
                exit()


def main():
    manager = FileManager()
    manager.CLI()


if __name__ == '__main__':
    main()
