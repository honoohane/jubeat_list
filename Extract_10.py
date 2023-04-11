import pandas as pd

data = pd.read_csv('jubeat_list.csv')
output = pd.DataFrame(columns=['title', 'level', '体力', '发狂', '节奏', '手法', '认识'])

for index, row in data.iterrows():
    if row['bsc_level'] >= 10:
        output = output.append({'title': row['title'] + '(BSC)', 'level': row['bsc_level']}, ignore_index=True)
        flag = 1
    if row['adv_level'] >= 10:
        output = output.append({'title': row['title'] + '(ADV)', 'level': row['adv_level']}, ignore_index=True)
        flag = 1
    if row['ext_level'] >= 10:
        if flag == 1:
            output = output.append({'title': row['title'] + '(EXT)', 'level': row['ext_level']}, ignore_index=True)
        else:
            output = output.append({'title': row['title'], 'level': row['ext_level']}, ignore_index=True)
    flag = 0

output.to_csv('jubeat_lv10.csv', index=False, encoding='utf_8_sig', quoting=1)