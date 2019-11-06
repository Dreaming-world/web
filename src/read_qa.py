from collections import defaultdict
import numpy as np

'''
dict key--index [0 1] [0]--qa [1] question
'''
chart_list = ['B', 'C', 'D', 'E', 'F']


def split_answer(answer):
    result = []
    index = 0
    for key in chart_list:
        if key in answer:
            ele = answer.split(key)[0]
            answer = answer[len(ele):]
            result.append(ele)
            index = index + 1
    result.append(answer)
    return result


def read_qa(file_path, choice=[]):
    singal_dict = defaultdict(list)
    double_dict = defaultdict(list)
    fill_dict = {}
    index_singal = 0
    index_double = 0
    index_fill = 0
    flag_singal = 0
    flag_double = 0
    flag_fill = 0
    with open(file_path, "r") as f:
        line = f.readline().replace('\n', '').replace('\t', '')
        while line:
            if "单选题" in line:
                flag_singal = 1
                flag_double = 0
                flag_fill = 0
                line = f.readline().replace('\n', '').replace('\t', '')
            elif "多选题" in line:
                flag_singal = 0
                flag_double = 1
                flag_fill = 0
                line = f.readline().replace('\n', '').replace('\t', '')
            elif "填空题" in line:
                flag_singal = 0
                flag_double = 0
                flag_fill = 1
                line = f.readline().replace('\n', '').replace('\t', '')
            if flag_singal:
                # line = f.readline()
                if 'A' not in line and 'B' not in line and 'C' not in line and 'D' not in line:
                    index_singal += 1
                    qa = line.split('.')[1]
                    # print(qa)
                    singal_dict[index_singal].append(qa)
                    line = f.readline().replace('\n', '').replace('\t', '')
                    answer = ''
                    while 'A' in line or 'B' in line or 'C' in line or 'D' in line:
                        answer += line
                        line = f.readline().replace('\n', '').replace('\t', '')
                    singal_dict[index_singal].append(split_answer(answer.replace(' ', '')))
                    # print(answer)

            if flag_double:
                # line = f.readline()
                if 'A' not in line and 'B' not in line and 'C' not in line and 'D' not in line:
                    index_double += 1
                    qa = line.split('.')[1]
                    # print(qa)
                    double_dict[index_double].append(qa)
                    line = f.readline().replace('\n', '').replace('\t', '')
                    answer = ''
                    while 'A' in line or 'B' in line or 'C' in line or 'D' in line or 'E' in line:
                        answer += line + ' '
                        line = f.readline().replace('\n', '').replace('\t', '')
                    double_dict[index_double].append(split_answer(answer.replace(' ', '')))
                    # print(answer)

            if flag_fill:
                index_fill += 1
                fill_dict[index_fill]= ''.join(line.split('.')[1:])
                # print(line)
                line = f.readline().replace('\n', '').replace('\t', '')
    # TODO
    single_choice = np.random.choice(a=index_singal, size=choice[0], replace=False, p=None)
    double_choice = np.random.choice(a=index_double, size=choice[1], replace=False, p=None)
    fill_choice = np.random.choice(a=index_fill, size=choice[2], replace=False, p=None)
    dict_singal = defaultdict()
    dict_double = defaultdict()
    dict_fill = defaultdict()
    new_index = 1
    for index in single_choice:
        dict_singal[new_index] = singal_dict[index + 1]
        new_index += 1
    new_index = 1
    for index in double_choice:
        dict_double[new_index] = double_dict[index + 1]
        new_index += 1
    new_index = 1
    for index in fill_choice:
        dict_fill[new_index] = fill_dict[index + 1]
        new_index += 1
    return dict_singal, dict_double, dict_fill


if __name__ == "__main__":
    file_path = '../qa_source/qa.txt'
    dict_singal, dict_double, dict_fill = read_qa(file_path, choice=[2, 1, 1])
    print(dict_singal, dict_double, dict_fill)

