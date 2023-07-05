import json
from datetime import datetime
import base64
from docx import Document
from utils import *
from Python_SDK.test_code.OCRTest import request_smartstructure_file, request_webimage_file

id = 1
image_path = f'dataset_CV/base64/images/{id}_01.png'
def datahanding(resume_base):
    output = {}  # 原始输出数据
    output_handle = {'姓名': '吴彦祖', '年龄': 23, '最高学历': '无', '毕业院校': '无', '工作年限': '无'}  # 处理后的输出数据

    # 使用webimage接口读取数据
    data_str = request_webimage_file(resume_base)
    wordlist = []  # 所有文字的字符串数组
    for item in data_str['body']['content']['prism_wordsInfo']:
        wordlist.append(f'{item["word"]}')  # 生成字符串数组
    wordstr = ''.join(wordlist)
    print(f"简历所有词条为：{wordlist}\n")

    # 使用智能结构化接口读取数据
    data = request_smartstructure_file(resume_base)
    birthday = None
    age_count = 0
    for item in data['recognize_list'][0]['item_content']['item_list']:
        name = item['name']
        content = item['content']
        output[name] = content  # 智能解析出来的特征字典
        # 处理姓名
        if item['name'] == '姓名':
            output_handle['姓名'] = item['content']
        # 处理年龄
        if item['name'] in ['出生', '出生年月', '生日', '出生日期']:
            age_count += 1
            print("开始处理年龄")
            birthday = item['content']
            print(f"birthday = {birthday}")
            if birthday:
                if '.' in birthday:  # 判断是否为形如"1996.05"的格式
                    birthday = datetime.strptime(birthday, '%Y.%m')
                elif '日' in birthday:  # 其他情况，默认为"1990年2月"的格式,判断是否为"1990年2月10日的格式"
                    # 去除日期字符串中的"日"
                    birthday = birthday.replace("日", "")
                    birthday = datetime.strptime(birthday, '%Y年%m月%d')
                else:  # 默认为"1990年2月"的格式
                        birthday = datetime.strptime(birthday, '%Y年%m月')
                age = datetime.now().year - birthday.year
                output_handle['年龄'] = age + 1  # 官方标注信息年龄均大一岁
                print(f'格式转换过后的实际年龄: {age}')
            else:
                print('出生年月数据为空')
        elif item['name'] in ['年龄']:
            age_count += 1
            print("开始处理年龄")
            age = item['content']
            output_handle['年龄'] = age
            print(f'格式转换过后的实际年龄: {age}')
    if age_count == 0:
        print("未找到出生年月数据")
    print(f"智能结构化识别的结果：{output}\n")

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


if __name__ == "__main__":
    datahanding(image_path)
