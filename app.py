import os, itertools, time

char_range = '0123456789'
password = '1024'
failed_str = '땡'

pw_len = len(password)
per = list(itertools.product(char_range[:], repeat=pw_len))

parent_path = 'Outputs/' + str(time.time() * 1000).split('.')[0] + '/'

for e in per:
    path = parent_path + '/'.join(e)
    os.makedirs(path)
    with open(path + '/' + failed_str, 'w', encoding='utf-8') as f: f.write(failed_str)