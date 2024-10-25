from сaesarCipher import CaesarCipher

def main():

    # Чтение файла с открытым текстом
    input_file = 'files/input.txt'
    with open(input_file, 'r') as file:
        plaintext = file.read().strip().lower()

    # Ключевое слово
    keyword = input("Введите ключевое слово: ").lower()

    # Создаем объект класса CaesarCipher
    cipher = CaesarCipher(keyword)

    # Шифрование
    encrypted_text = cipher.encrypt(plaintext)
    print("Зашифрованный текст:")
    print(encrypted_text)

    # Запись зашифрованного текста в файл
    with open('files/encrypted.txt', 'w') as file:
        file.write(encrypted_text)

    # Дешифрование
    decrypted_text = cipher.decrypt(encrypted_text)
    print("\nДешифрованный текст:")
    print(decrypted_text)

    # Запись дешифрованного текста в файл
    with open('files/decrypted.txt', 'w') as file:
        file.write(decrypted_text)


if __name__ == "__main__":
    main()
