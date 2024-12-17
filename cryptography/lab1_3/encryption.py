class Encryptor:
    def __init__(self, lfsr1_init, lfsr2_init, feedback1, feedback2):
        """
        Инициализация ЛРС и полиномов обратной связи.
        """
        self.lfsr1 = lfsr1_init
        self.lfsr2 = lfsr2_init
        self.feedback1 = feedback1
        self.feedback2 = feedback2

    def lfsr(self, register, feedback_coeffs):
        """
        Функция ЛРС.
        Принимает регистр и полином обратной связи (коэффициенты).
        """
        feedback = 0
        for coeff in feedback_coeffs:
            feedback ^= (register >> coeff) & 1
        register = (register << 1) & 0xFFFFFFFF
        register |= feedback
        return register

    def encrypt_decrypt(self, text):
        """
        Функция шифрования/дешифрования.
        Сначала сдвигаем ЛРС и генерируем новый бит гаммы,
        затем применяем его к символу.
        """
        result_text = ''
        for char in text:
            # Сдвигаем ЛРС перед вычислением гаммы
            self.lfsr1 = self.lfsr(self.lfsr1, self.feedback1)
            self.lfsr2 = self.lfsr(self.lfsr2, self.feedback2)

            # Извлекаем биты для формирования гаммы
            bit1 = self.lfsr1 & 1
            bit2 = self.lfsr2 & 1

            # Вычисляем гамму
            gamma = bit1 ^ bit2

            # Применяем XOR к символу с гаммой
            result_char = chr(ord(char) ^ gamma)
            result_text += result_char

        return result_text

    def reset(self, lfsr1_init, lfsr2_init):
        """
        Сброс ЛРС для повторного использования.
        """
        self.lfsr1 = lfsr1_init
        self.lfsr2 = lfsr2_init
