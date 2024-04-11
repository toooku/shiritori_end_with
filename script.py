import collections
import csv


def main():
    with open('input_data/lex_3_1.csv') as f:
        reader = csv.reader(f)
        reader_list = [row for row in reader]

    lexeme_reading_list = []

    for row in reader_list:
        if row[4] == '名詞':
            lexeme_reading_list.append(row[10])

    end_word_list = []
    for lexeme in lexeme_reading_list:
        end_word = lexeme[-1]
        end_word_list.append(end_word)

    count_end_word = collections.Counter(end_word_list)
    data = [{'word': key, 'count': value} for key, value in
            sorted(count_end_word.items(), key=lambda item: item[1], reverse=True)]

    field_name = ['word', 'count']
    with open(r'result/result.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_name)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    main()
