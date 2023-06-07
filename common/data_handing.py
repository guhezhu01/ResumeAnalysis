import json
from datetime import datetime
from utils import *
from Python_SDK.test_code.OCRTest import request_smartstructure_file, request_webimage_file

imagepath = 'dataset_CV/base64/15_01.png'


def datahanding(imagepath):
    output = {}  # 原始输出数据
    output_handle = {'姓名': '无', '年龄': 23, '最高学历': '无', '毕业院校': '无', '工作年限': '无'}  # 处理后的输出数据

    # 使用webimage接口读取数据
    data_str = request_webimage_file(imagepath)
    wordlist = []
    for item in data_str['body']['content']['prism_wordsInfo']:
        wordlist.append(f'{item["word"]}')  # 生成字符串数组
    wordstr = ''.join(wordlist)
    print(f"简历所有词条为：{wordlist}\n")

    # 使用智能结构化接口读取数据
    data = request_smartstructure_file(imagepath)
    birthday = None
    for item in data['recognize_list'][0]['item_content']['item_list']:
        name = item['name']
        content = item['content']
        output[name] = content
        # 处理姓名
        if item['name'] == '姓名':
            output_handle['姓名'] = item['content']
        # 处理年龄
        if item['name'] in ['出生', '出生年月', '生日', '出生日期']:
            birthday = item['content']
            if birthday:
                birthday = datetime.strptime(birthday, '%Y年%m月')
                age = datetime.now().year - birthday.year
                output_handle['年龄'] = age + 1  # 官方标注信息年龄均大一岁
                print(f'格式转换过的，年龄: {age}')
            else:
                print('未找到出生年月数据')
    print(f"智能结构化识别的结果：{output}\n")

    # webimage接口中将所有的词条全部以字符串数组的形式打印
    # id_str = 15
    # with open(f'test/response_{id_str}_webimage.json', 'r', encoding='utf-8') as f:
    #     data_str = json.load(f) # dict格式
    # wordlist = []
    # for item in data_str['body']['content']['prism_wordsInfo']:
    #     wordlist.append(f'{item["word"]}')  # 生成字符串数组
    # wordstr = ''.join(wordlist)
    # print(f"简历所有词条为：{wordlist}\n")

    # 读取文件数据
    # id = 15
    # with open(f'test/response_{id}.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    #
    # birthday = None
    #
    # for item in data['recognize_list'][0]['item_content']['item_list']:
    #     name = item['name']
    #     content = item['content']
    #     output[name] = content
    #     # 处理姓名
    #     if item['name'] == '姓名':
    #         output_handle['姓名'] = item['content']
    #     # 处理年龄
    #     if item['name'] in ['出生', '出生年月', '生日', '出生日期']:
    #         birthday = item['content']
    #         if birthday:
    #             birthday = datetime.strptime(birthday, '%Y年%m月')
    #             age = datetime.now().year - birthday.year
    #             output_handle['年龄'] = age + 1  # 官方标注信息年龄均大一岁
    #             print(f'格式转换过的，年龄: {age}')
    #         else:
    #             print('未找到出生年月数据')
    # print(f"智能结构化识别的结果：{output}\n")

    # 获取最高学历
    education = extract_education(wordstr)
    output_handle['最高学历'] = education
    # print(education)

    # 获取毕业院校
    school = get_school_name(wordlist)  # 传入字符串数组
    output_handle['毕业院校'] = school
    # print(school)

    # 获取工作年限
    work_years = calculate_work_years(wordlist)  # 最大时间减去简历最小时间
    # 计算实际的工作年限差
    diff_workYears = calculate_education_diff(work_years, education)
    if diff_workYears is not None:
        output_handle['工作年限'] = diff_workYears
        # print(f"工作年限与学历对应数字的差值：{diff}")
    else:
        output_handle['工作年限'] = work_years
        print("无效的学历信息")
    # print(f"工作年限：{work_years}")

    print(f"按照要求提取出来的关键信息：\n{output_handle}\n")
    return output_handle
    # with open(f'output_{id}.json', 'w') as f:
    #     json.dump(output, f)
    # with open(f'output_handle_{id}.json', 'w') as f:
    #     json.dump(output_handle, f)


if __name__ == "__main__":
    datahanding(imagepath)
