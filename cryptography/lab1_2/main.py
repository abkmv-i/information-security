import os
from file_crypto import encrypt_file, decrypt_file

def main():
    # Главная функция программы
    key = 'Это секретный ключик'.encode('utf-8')[:16]
    input_filename = 'files/input.txt'  # Путь к входному файлу
    encrypted_filename = 'files/encrypted.bin'  # Путь к выходному зашифрованному файлу
    decrypted_filename = 'files/decrypted.txt'  # Путь к выходному расшифрованному файлу

    # Проверяем наличие входного файла
    if not os.path.exists(input_filename):
        print(f"Входной файл {input_filename} не найден.")
        return

    # Шифруем входной файл
    encrypt_file(input_filename, encrypted_filename, key)
    print(f"Файл {input_filename} успешно зашифрован в {encrypted_filename}.")

    # Дешифруем зашифрованный файл
    decrypt_file(encrypted_filename, decrypted_filename, key)
    print(f"Файл {encrypted_filename} успешно расшифрован в {decrypted_filename}.")

if __name__ == '__main__':
    main()
