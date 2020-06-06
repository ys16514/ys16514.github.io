'''
@Author: sunyudi
@Date: 2020-06-06 13:07:30
@LastEditTime: 2020-06-06 13:25:32
'''
import os

origin_module_list = []
for root, dirs, files in os.walk('.'):
    for _dir in dirs:
        if _dir.startswith('.'):
            continue
        if _dir == 'assets':
            continue
        origin_module_list.append(_dir)
    break

valid_module_list = []
for module in origin_module_list:
    for root, _, files in os.walk(module):
        found_index_md = False
        for _file in files:
            if _file == 'index.md':
                found_index_md = True
                break
        if not found_index_md:
            print("Module {0} doesn't have index.md".format(module))
        else:
            valid_module_list.append(module)
        break

with open('_navbar.md', 'w', encoding='utf-8') as fp:
    for module in valid_module_list:
        content = '* [{0}](/{0}/index.md)\n'.format(module)
        fp.write(content)

with open('_sidebar.md', 'w', encoding='utf-8') as fp:
    fp.write('* [Home](/)\n')
    for module in valid_module_list:
        content = '* [{0}](/{0}/index.md)\n'.format(module)
        fp.write(content)