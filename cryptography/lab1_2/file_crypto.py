from tea import TEA


# Функция для шифрования файла
def encrypt_file(input_filename, output_filename, key):
    # Создаем экземпляр шифра TEA с заданным ключом
    tea = TEA(key)

    # Открываем входной файл для чтения в бинарном режиме и выходной файл для записи в бинарном режиме
    with open(input_filename, 'rb') as infile, open(output_filename, 'wb') as outfile:
        while True:
            # Читаем блок размером 8 байт из входного файла
            block = infile.read(8)
            # Если блок пустой (конец файла), выходим из цикла
            if len(block) == 0:
                break
            # Если размер блока меньше 8 байт, добавляем padding нулями до 8 байт
            if len(block) < 8:
                block = block.ljust(8, b'\0')  # Добавляем padding
            # Шифруем блок с помощью алгоритма TEA
            encrypted_block = tea.encrypt(block)
            # Записываем зашифрованный блок в выходной файл
            outfile.write(encrypted_block)


# Функция для дешифрования файла
def decrypt_file(input_filename, output_filename, key):
    # Создаем экземпляр шифра TEA с заданным ключом
    tea = TEA(key)

    # Открываем входной файл для чтения в бинарном режиме и выходной файл для записи в бинарном режиме
    with open(input_filename, 'rb') as infile, open(output_filename, 'wb') as outfile:
        while True:
            # Читаем блок размером 8 байт из входного файла
            block = infile.read(8)
            # Если блок пустой (конец файла), выходим из цикла
            if len(block) == 0:
                break
            # Дешифруем блок с помощью алгоритма TEA
            decrypted_block = tea.decrypt(block)
            # Убираем padding из дешифрованного блока и записываем его в выходной файл
            outfile.write(decrypted_block.rstrip(b'\0'))  # Убираем padding
