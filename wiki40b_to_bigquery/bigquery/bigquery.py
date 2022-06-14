from mimetypes import init
import time
from google.cloud import bigquery


class MyBigquery():
    SCHEMA = [
        bigquery.SchemaField("sentence", "STRING", mode="REQUIRED"),
    ]
    # bigquery limit is 10000
    MAX_INSERT_RECORDS_NUM = 1000

    def __init__(self, language_code) -> None:
        self.client = bigquery.Client().from_service_account_json(
            '/Users/kitanotoshiyuki/wiki40b_to_bigquery/anki-like-listening-app-df24f-ea0764ec6e22.json')
        self.table_id = 'anki-like-listening-app-df24f.wiki40b.' + language_code
        self.table = bigquery.Table(self.table_id, schema=self.SCHEMA)
        # TODO create table if none

    def create_wiki40b_table(self):
        schema = [
            bigquery.SchemaField("sentence", "STRING", mode="REQUIRED"),
        ]
        table = bigquery.Table(self.table_id, schema=schema)
        table = self.client.create_table(table)  # Make an API request.
        print(
            "Created table {}.{}.{}".format(
                table.project, table.dataset_id, table.table_id)
        )

    def insert_paragraphs(self, paragraphs):

        records = [{'sentence': p} for p in paragraphs]
        for i in range(0, len(records), self.MAX_INSERT_RECORDS_NUM):
            errors = self.client.insert_rows_json(
                self.table, records[i:i+self.MAX_INSERT_RECORDS_NUM])
            if errors != []:
                print("Encountered errors while inserting rows: {}".format(errors))

    def create_index(self,):
        QUERY = '''
            CREATE SEARCH INDEX my_index
            ON {}(sentence);
        '''.format(self.table_id)
        print('QUERY is :', QUERY)
        result = self.client.query(QUERY)
        print(result)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # TODO? guess soruce language from words file
    parser.add_argument("-l", "--language_code",
                        help="wiki40b language code: https://research.google/pubs/pub49029/?hl=ja")
    args = parser.parse_args()
    x = MyBigquery(args.language_code)
    # x.create_wiki40b_table()
    x.create_index()
