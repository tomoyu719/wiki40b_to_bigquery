import os

import tensorflow_datasets as tfds


def decode_wiki40b(language_code):
    # ds = tfds.load(os.path.join('wiki40b/', language_code), split='train')
    ds = tfds.load(os.path.join('wiki40b/', language_code), split='test')
    start_paragraph = False
    for wiki in ds.as_numpy_iterator():
        for text in wiki['text'].decode().split('\n'):
            if start_paragraph:
                text = text.split('_NEWLINE_')
                yield text
                start_paragraph = False
            if text == '_START_PARAGRAPH_':
                start_paragraph = True
