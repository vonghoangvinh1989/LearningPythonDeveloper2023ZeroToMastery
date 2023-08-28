# r: read mode
# w: write mode, if file does not exist, it creates new file, if file exists rewrite the content
# a: append mode, append the content to the file
# r+: read and write mode, replace the content of file based on length of content

try:
    with open('sad.txt', mode='x') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
