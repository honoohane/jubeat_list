import pandas as pd
from collections import defaultdict

def extract_level_10():
    data = pd.read_csv('output/jubeat_list.csv')
    csv_output_list = []
    xlsx_output_list = []
    level_groups = defaultdict(list)

    for index, row in data.iterrows():
        flag = 0
        try:
            bsc_level = float(row['bsc_level'])
            if bsc_level >= 10:
                csv_record = {'title': row['title'] + '(BSC)', 'level': bsc_level}
                csv_output_list.append(csv_record)
                xlsx_record = {'title': row['title'] + '(BSC)', 'level': bsc_level,
                              'actual_level': '', '体力': '', '发狂': '', '节奏': '', '手法': '', '认识': ''}
                xlsx_output_list.append(xlsx_record)
                level_key = f"{bsc_level:.1f}"
                level_groups[level_key].append(xlsx_record)
                flag = 1
        except (ValueError, TypeError):
            pass

        try:
            adv_level = float(row['adv_level'])
            if adv_level >= 10:
                csv_record = {'title': row['title'] + '(ADV)', 'level': adv_level}
                csv_output_list.append(csv_record)
                xlsx_record = {'title': row['title'] + '(ADV)', 'level': adv_level,
                              'actual_level': '', '体力': '', '发狂': '', '节奏': '', '手法': '', '认识': ''}
                xlsx_output_list.append(xlsx_record)
                level_key = f"{adv_level:.1f}"
                level_groups[level_key].append(xlsx_record)
                flag = 1
        except (ValueError, TypeError):
            pass

        try:
            ext_level = float(row['ext_level'])
            if ext_level >= 10:
                if flag == 1:
                    title_with_diff = row['title'] + '(EXT)'
                else:
                    title_with_diff = row['title']
                csv_record = {'title': title_with_diff, 'level': ext_level}
                csv_output_list.append(csv_record)
                xlsx_record = {'title': title_with_diff, 'level': ext_level,
                              'actual_level': '', '体力': '', '发狂': '', '节奏': '', '手法': '', '认识': ''}
                xlsx_output_list.append(xlsx_record)
                level_key = f"{ext_level:.1f}"
                level_groups[level_key].append(xlsx_record)
        except (ValueError, TypeError):
            pass

    csv_output = pd.DataFrame(csv_output_list)
    csv_output.to_csv('output/jubeat_lv10.csv', index=False, encoding='utf_8_sig', quoting=1)

    with pd.ExcelWriter('output/jubeat_lv10_by_level.xlsx', engine='openpyxl') as writer:
        for level in sorted(level_groups.keys(), key=lambda x: float(x), reverse=True):
            df = pd.DataFrame(level_groups[level])
            df = df.sort_values('title')
            df.to_excel(writer, sheet_name=level, index=False)
