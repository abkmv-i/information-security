class CaesarCipher:
    def __init__(self, keyword):
        # Определяем русский алфавит для строчных букв
        self.lowercase_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        # То же самое для заглавных букв
        self.uppercase_alphabet = self.lowercase_alphabet.upper()
        # Приводим ключевое слово к нижнему регистру
        self.keyword = keyword.lower()
        # Создаем шифрованные алфавиты на основе ключевого слова для строчных и заглавных букв
        self.cipher_lowercase_alphabet = self.generate_cipher_alphabet(self.lowercase_alphabet)
        self.cipher_uppercase_alphabet = self.cipher_lowercase_alphabet.upper()

    def generate_cipher_alphabet(self, alphabet):
        """
        Генерирует шифрованный алфавит на основе ключевого слова.
        Ключевое слово перемещается в начало алфавита, удаляя дубликаты букв.
        Оставшаяся часть алфавита заполняется буквами, которых нет в ключе.
        """
        # Удаляем повторяющиеся символы из ключевого слова, сохраняя их первый вход
        keyword = ''.join(sorted(set(self.keyword), key=self.keyword.index))
        # Генерируем модифицированный алфавит:
        # сначала идут буквы из ключевого слова, затем оставшиеся буквы из алфавита
        cipher_alphabet = keyword + ''.join([ch for ch in alphabet if ch not in keyword])
        return cipher_alphabet

    def encrypt(self, text):
        """
        Шифрует переданный текст, заменяя буквы по шифрованному алфавиту.
        Строчные и заглавные буквы обрабатываются отдельно.
        """
        encrypted_text = []  # Список для хранения зашифрованного текста
        for char in text:
            if char in self.lowercase_alphabet:
                # Если символ в нижнем регистре, заменяем его на соответствующий символ из шифрованного алфавита
                index = self.lowercase_alphabet.index(char)
                encrypted_text.append(self.cipher_lowercase_alphabet[index])
            elif char in self.uppercase_alphabet:
                # Если символ в верхнем регистре, делаем замену по заглавному шифрованному алфавиту
                index = self.uppercase_alphabet.index(char)
                encrypted_text.append(self.cipher_uppercase_alphabet[index])
            else:
                # Если символ не является буквой алфавита (например, пробел или знак), оставляем его без изменений
                encrypted_text.append(char)
        # Преобразуем список символов в строку и возвращаем результат
        return ''.join(encrypted_text)

    def decrypt(self, text):
        """
        Дешифрует текст, выполняя обратную замену символов по исходному алфавиту.
        """
        decrypted_text = []  # Список для хранения дешифрованного текста
        for char in text:
            if char in self.cipher_lowercase_alphabet:
                # Если символ в нижнем регистре, находим его индекс в шифрованном алфавите и заменяем на исходную букву
                index = self.cipher_lowercase_alphabet.index(char)
                decrypted_text.append(self.lowercase_alphabet[index])
            elif char in self.cipher_uppercase_alphabet:
                # Для заглавных символов аналогично, но используем заглавный шифрованный алфавит
                index = self.cipher_uppercase_alphabet.index(char)
                decrypted_text.append(self.uppercase_alphabet[index])
            else:
                # Символы вне алфавита не дешифруем и оставляем их как есть
                decrypted_text.append(char)
        # Преобразуем список символов в строку и возвращаем результат
        return ''.join(decrypted_text)
