from classes import Player
from function import load_random_word

user_names = input("Ввведите имя игрока\n")

player = Player(user_names)  # Экземпляр класса игрока

if player.len_name(user_names):
    print(f"Привет, {player}!")

random_words = load_random_word()  # Переменая для функции получения рандомного слова.

print(f"Составьте {len(random_words.count_subwords())} слов из слова - {random_words}")

print(f"Слова должны быть не короче 3 букв\nПоехали, ваше первое слово?")

for random_word in random_words.subwords:
    user_input = input()
    if user_input in random_words.subwords:
        if not user_input in player.use_words:
            player.add_used_word(user_input)
            print("Верно 😇 ")
        elif player.is_word_unused(user_input):
            print("Слово уже есть 😈 ")
    if random_words.stop_games(user_input):
        print(f"Игра завершена!\nВы угадали {player.word_count()} слова")
        break
    if random_words.min_len(user_input):
        print("Слова должны быть не короче 3 букв")
    elif not user_input in player.use_words:
        print("Нет допустимх слов 😛 ")
else:
    print(f"Cлова закончились игра завершена!\nВы угадали {player.word_count()} слов")
