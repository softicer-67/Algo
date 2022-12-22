from functions import *


def select_sorted(sort_columns=None, limit=5, group_by_name=False, order='desc', filename='dump.csv'):

    file = load_file()
    res = []
    arr = []

    arg = {
        'sort_columns': sort_columns,
        'group_by_name': group_by_name,
        'order': order,
        'limit': limit,
        'filename': filename
    }

    for k, v in arg.items():
        arr.append({
            'command_name': k,
            'value': v
        })

    try:
        for idx, item in enumerate(arr):

            if item['command_name'] == 'sort_columns':
                res = filter_func(item['value'], file)

            elif item['command_name'] == 'group_by_name':
                res = sort_func(item['value'], res)

            elif item['command_name'] == 'order':
                res = sort_revers(item['value'], res)

            elif item['command_name'] == 'limit':
                res = limit_func(int(item['value']), res)

            elif item['command_name'] == 'filename':
                write_file(item['value'], res)

    except IndexError:
        print('Ошибка ввода')
        quit()

    for item in res:
        res = str(item).split(',')
        print(f"{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]} | {res[6]}")


if __name__ == '__main__':
    # select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv')
    select_sorted(sort_columns=['high'], order='asc', limit=10, filename='dump.csv')
