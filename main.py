import os
import shutil

min_style_index = 95    # style to generate (min)
max_style_index = 99    # style to generate (max)

read_index = '38'   # change ¸Ó¸®38_¿©_2.pal depending on number
prefix = '®'        # char before read_index
suffix = '_'        # char after read_index
input_path = '.\\m'
# input_path = '.\\f'
output_path = '.\\out'


def main():
    count = 0
    for root, dirs, files in os.walk(input_path):
        for filename in files:
            old_name = os.path.join(input_path, filename)
            for new_index in range(min_style_index, max_style_index + 1):
                new_name = os.path.join(output_path, filename.replace(f'{prefix}{read_index}{suffix}',
                                                                      f'{prefix}{new_index}{suffix}'))
                print('new:', new_name)
                count += 1
                shutil.copy(old_name, new_name)


if __name__ == '__main__':
    main()
