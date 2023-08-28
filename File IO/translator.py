from translate import Translator


def get_content(filepath):
    try:
        with open(filepath, mode='r', encoding="utf-8") as test_file:
            return test_file.readlines()
    except FileNotFoundError as err:
        print(f'Check your file path {err}')
        return []
    except IOError as err:
        print(f'Error happened {err}')
        return []


def translation(language_code, content_list):
    translator = Translator(to_lang=language_code)
    return [translator.translate(sentence) for sentence in content_list]


def write_new_file(filepath, content_list):
    try:
        with open(filepath, mode='w', encoding="utf-8") as write_file:
            for line in content_list:
                write_file.write(f'{line}\n')
    except FileNotFoundError as err:
        print(f'Check your file path {err}')
    except IOError as err:
        print(f'Error happened {err}')


language_code = 'vi'
content_list = get_content('./test.txt')

result_list = translation(language_code, content_list)
write_new_file('test2.txt', result_list)
