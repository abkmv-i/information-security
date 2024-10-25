class FileHandler:
    @staticmethod
    def read_file(filename):
        """
        Чтение текста из файла.
        """
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_file(filename, text):
        """
        Запись текста в файл.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
