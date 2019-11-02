from collections import defaultdict

'''
dict key--index [0 1] [0]--qa [1] question
'''

def read_qa(file_path):
    singal_dict = defaultdict(list)
    double_dict = defaultdict(list)
    fill_dict = defaultdict(list)
    index_singal = 0
    index_double = 0
    index_fill = 0
    flag_singal = 0
    flag_double = 0
    flag_fill = 0
    with open('../qa_source/qa.txt', "r") as f:
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
                    qa = line
                    print(qa)
                    singal_dict[index_singal].append(qa)
                    line = f.readline().replace('\n', '').replace('\t', '')
                    answer = ''
                    while 'A' in line or 'B' in line or 'C' in line or 'D' in line:
                        answer += line + ' '
                        line = f.readline().replace('\n', '').replace('\t', '')
                    singal_dict[index_singal].append(answer.split())
                    print(answer)

            if flag_double:
                # line = f.readline()
                if 'A' not in line and 'B' not in line and 'C' not in line and 'D' not in line:
                    index_double += 1
                    qa = line
                    print(qa)
                    double_dict[index_double].append(qa)
                    line = f.readline().replace('\n', '').replace('\t', '')
                    answer = ''
                    while 'A' in line or 'B' in line or 'C' in line or 'D' in line or 'E' in line:
                        answer += line +' '
                        line = f.readline().replace('\n', '').replace('\t', '')
                    double_dict[index_double].append(answer)
                    print(answer)

            if flag_fill:
                index_fill += 1
                fill_dict[index_fill].append(line)
                print(line)
                line = f.readline().replace('\n', '').replace('\t', '')
    return singal_dict, double_dict, fill_dict


if __name__ == "__main__":
    singal_dict, double_dict, fill_dict = read_qa('hh')

