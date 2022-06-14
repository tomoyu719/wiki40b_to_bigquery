import argparse
from wiki40b_to_bigquery.bigquery.bigquery import MyBigquery
# from wiki40b_to_bigquery.bigquery import bigquery

from wiki40b_to_bigquery.text_utils.text_utils import TextUtils
from wiki40b_to_bigquery.wiki40b.decode_wiki40b import decode_wiki40b

# avoid memory leak
MAX_PROCESS_PARAGRAPH_NUM_AT_ONCE = 100000


def main():
    parser = argparse.ArgumentParser()

    # TODO? guess soruce language from words file
    parser.add_argument("-l", "--language_code",
                        help="wiki40b language code: https://research.google/pubs/pub49029/?hl=ja")

    # TODO validation
    args = parser.parse_args()
    language_code = args.language_code
    wiki40b = decode_wiki40b(language_code)
    bigquery = MyBigquery(language_code)
    paragraphs = []
    for wiki_text in wiki40b:
        paragraphs += wiki_text
        if len(paragraphs) >= MAX_PROCESS_PARAGRAPH_NUM_AT_ONCE:
            bigquery.insert_paragraphs(paragraphs)
            paragraphs = []
    bigquery.insert_paragraphs(paragraphs)
