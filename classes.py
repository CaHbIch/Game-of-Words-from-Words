class BasicWord:

    def __init__(self, word, subwords):
        self.word = word  # исходное слово
        self.subwords = subwords  # набор допустимых подслов.
        self.user_input = None

    @classmethod
    def stop_games(cls, user_input):
        if user_input == 'стоп':
            return user_input

    def min_len(cls, user_input):
        if len(user_input) < 3:
            return user_input

    def words(self):
        """проверка введенного слова в списке допустимых подслов"""
        if self.subwords == self.user_input:
            return True

    def count_subwords(self):
        """подсчет количества подслов."""
        return self.subwords

    def __repr__(self):
        return self.word


class Player:

    def __init__(self, name):
        self.__name = name  # имя пользователя,
        self.use_words = []  # использованные слова пользователя.

    @classmethod
    def len_name(cls, name):
        if len(name) >= 3:
            return name
        else:
            raise ValueError("Игровое имя меньше 3 букв ")

    def word_count(self):
        """получение количества слов"""
        return len(self.use_words)

    def add_used_word(self, user_input):
        """добавление слова в использованные слова"""
        if user_input in self.use_words:
            return None
        else:
            self.use_words.append(user_input)

    def is_word_unused(self, user_input):
        """проверка использования данного слова до этого"""
        if self.use_words:
            return True
        return False

    def __repr__(self):
        return self.__name
