import sys
import os
from PIL import Image

# grab first and second arguments
first_argument = sys.argv[1]
second_argument = sys.argv[2]

print(
    f'first_argument is {first_argument}, second argument is {second_argument}')

# check is new/ exists, if not create
# clean the path of new folder
if not os.path.exists(second_argument):
    os.mkdir(second_argument)
else:
    print(f'Folder {second_argument} already exists')

# loop through Pokedex, convert images to png
# for file_name in os.scandir(first_argument):
#     if file_name.is_file():
#         img = Image.open(file_name.path)
#         new_file_name = file_name.name.split('.')[0]
#         img.save(f'{second_argument}/{new_file_name}.png', 'png')
#         print('all done!')

for file_name in os.listdir(first_argument):
    img = Image.open(f'{first_argument}{file_name}')
    clean_name = os.path.splitext(file_name)[0]
    print(clean_name)
    img.save(f'{second_argument}{clean_name}.png', 'png')
    print('all done!')
