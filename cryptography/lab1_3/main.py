from encryption import Encryptor
from file_operations import FileHandler


def main():
    # Инициализация ЛРС
    lfsr1_init = 0x80  # Начальное состояние ЛРС1
    lfsr2_init = 0x80  # Начальное состояние ЛРС2
    feedback1 = [80, 9, 4, 2, 0]  # Полином обратной связи ЛРС1
    feedback2 = [80, 5, 3, 2, 1, 0]  # Полином обратной связи ЛРС2

    # Создаем объект шифратора
    encryptor = Encryptor(lfsr1_init, lfsr2_init, feedback1, feedback2)

    # Файлы для работы
    input_file = 'files/input.txt'  # Файл с исходным текстом
    encrypted_file = 'files/encrypted.txt'  # Файл для зашифрованного текста
    decrypted_file = 'files/decrypted.txt'  # Файл для расшифрованного текста

    # Чтение исходного текста
    original_text = FileHandler.read_file(input_file)

    # Шифрование текста
    encrypted_text = encryptor.encrypt_decrypt(original_text)

    # Запись зашифрованного текста в файл
    FileHandler.write_file(encrypted_file, encrypted_text)

    # Сброс ЛРС для расшифровки
    encryptor.reset(lfsr1_init, lfsr2_init)

    # Расшифровка текста
    decrypted_text = encryptor.encrypt_decrypt(encrypted_text)

    # Запись расшифрованного текста в файл
    FileHandler.write_file(decrypted_file, decrypted_text)

    print(
        f"Тексты обработаны:\nИсходный текст в файле {input_file}\nЗашифрованный текст в файле {encrypted_file}\nРасшифрованный текст в файле {decrypted_file}")


# Вызов основной программы
if __name__ == "__main__":
    main()
