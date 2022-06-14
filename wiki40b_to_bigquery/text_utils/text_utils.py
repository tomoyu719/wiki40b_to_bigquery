import regex as re
import json
import random

# import MeCab
from nltk import sent_tokenize

NUM_STR = 'X'

# TODO fix duplicate implement
NGRAM_NUM = 3


class TextUtils():

    def __init__(self, language_code) -> None:
        self.language_code = language_code
        # self.is_nltk_tokenizer_supported_language = self.is_nltk_tokenizer_supported_language(
        #     language_code)
        # if language_code == 'ja':
        #     self.ja_tagger = MeCab.Tagger(
        #         '-O wakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    def text_to_sentences(self, text) -> list:
        # wiki40b
        # "en", "ar", "zh-cn", "zh-tw", "nl", "fr", "de", "it", "ja", "ko", "pl", "pt", "ru", "es", "th", "tr", "bg", "ca", "cs", "da", "el", "et", "fa", "fi", "he", "hi", "hr", "hu", "id", "lt", "lv", "ms", "no", "ro", "sk", "sl", "sr", "sv", "tl", "uk", "vi"
        # nltk
        # Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Italian, Norwegian, Polish, Portuguese, Russian, Slovene, Spanish, Swedish, Turkish
        if self.language_code == 'cz':
            return sent_tokenize(text, 'czech')
        elif self.language_code == 'da':
            return sent_tokenize(text, 'danish')
        elif self.language_code == 'nl':
            return sent_tokenize(text, 'dutch')
        elif self.language_code == 'en':
            return sent_tokenize(text, 'english')
        elif self.language_code == 'et':
            return sent_tokenize(text, 'estonian')
        elif self.language_code == 'fi':
            return sent_tokenize(text, 'finnish')
        elif self.language_code == 'fr':
            return sent_tokenize(text, 'french')
        elif self.language_code == 'de':
            return sent_tokenize(text, 'german')
        elif self.language_code == 'el':
            return sent_tokenize(text, 'greek')
        elif self.language_code == 'it':
            return sent_tokenize(text, 'italian')
        elif self.language_code in ['nn', 'no']:
            return sent_tokenize(text, 'norwegian')
        elif self.language_code == 'pl':
            return sent_tokenize(text, 'polish')
        elif self.language_code == 'pt':
            return sent_tokenize(text, 'portuguese')
        elif self.language_code == ['ru', 'uk']:
            return sent_tokenize(text, 'russian')
        elif self.language_code == 'sl':
            return sent_tokenize(text, 'slovene')
        elif self.language_code == 'es':
            return sent_tokenize(text, 'spanish')
        elif self.language_code == 'sv':
            return sent_tokenize(text, 'swedish')
        elif self.language_code == 'tr':
            return sent_tokenize(text, 'Turkish')
        elif self.language_code == 'ja':
            return text.split('。')
        else:
            return text.split('.')
