import json
import os

file_path = os.path.dirname(__file__)
class ReadFiles:
    def write_json(self, data, filename):

        file_name = file_path + os.sep + 'data' + os.sep + f'{filename}.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read_json(self, filename):
        file_name = file_path + os.sep + 'data' + os.sep + f'{filename}.json'
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)


if __name__ == '__main__':
    rf = ReadFiles()
    rf.write_json(123,'test')


