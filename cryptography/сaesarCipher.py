class CaesarCipher:
    def __init__(self, keyword):
        self.lowercase_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.uppercase_alphabet = self.lowercase_alphabet.upper()
        self.keyword = keyword.lower()
        self.cipher_lowercase_alphabet = self.generate_cipher_alphabet(self.lowercase_alphabet)
        self.cipher_uppercase_alphabet = self.cipher_lowercase_alphabet.upper()

    def generate_cipher_alphabet(self, alphabet):
        # Удаляем повторяющиеся символы из ключевого слова
        keyword = ''.join(sorted(set(self.keyword), key=self.keyword.index))
        # Создаем модифицированный алфавит
        cipher_alphabet = keyword + ''.join([ch for ch in alphabet if ch not in keyword])
        return cipher_alphabet

    def encrypt(self, text):
        encrypted_text = []
        for char in text:
            if char in self.lowercase_alphabet:
                index = self.lowercase_alphabet.index(char)
                encrypted_text.append(self.cipher_lowercase_alphabet[index])
            elif char in self.uppercase_alphabet:
                index = self.uppercase_alphabet.index(char)
                encrypted_text.append(self.cipher_uppercase_alphabet[index])
            else:
                encrypted_text.append(char)  # Не шифруем символы вне алфавита (например, пробелы, знаки)
        return ''.join(encrypted_text)

    def decrypt(self, text):
        decrypted_text = []
        for char in text:
            if char in self.cipher_lowercase_alphabet:
                index = self.cipher_lowercase_alphabet.index(char)
                decrypted_text.append(self.lowercase_alphabet[index])
            elif char in self.cipher_uppercase_alphabet:
                index = self.cipher_uppercase_alphabet.index(char)
                decrypted_text.append(self.uppercase_alphabet[index])
            else:
                decrypted_text.append(char)  # Не дешифруем символы вне алфавита
        return ''.join(decrypted_text)