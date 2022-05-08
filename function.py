from classes import BasicWord
import random
import requests
import json

def load_random_word():
    """получает список слов с внешнего ресурса и передает рандомное слово"""
    load_word = requests.get('https://jsonkeeper.com/b/VAI9') # получит список слов с внешнего ресурса,
    load_word_json = list(load_word.json())
    if not load_word:
        with open('word.json', encoding="utf-8") as file:
            load_word_json = json.load(file)
    get_random_words = random.choice(load_word_json) # выберет случайное слово
    basicword = BasicWord(get_random_words["word"], get_random_words["subwords"])
    return basicword

