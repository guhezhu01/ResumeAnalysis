import re
from datetime import datetime

# 获取最高学历
def extract_education(resume_text):
    # 定义学历列表
    education_list = ['博士', '硕士', '本科', '大专', '中专', '高中', '初中', '小学']
    # 将简历文本转换为小写字母
    resume_text = resume_text.lower()
    # 使用正则表达式匹配学历,从博士开始往小学检索
    for education in education_list:
        if re.search(education, resume_text):
            return education
    return '无'


# 获取最高学历的毕业院校
def get_school_name(resume_text):
    include_school = []
    dict = {}
    count, max = 0, 0
    for name in ['大学', '学院', '学校']:
        for j in resume_text:
            if name in j:
                include_school.append(j)  # 找到所有有关学校的词条

    # 找到含学校的数组中，出现次数最多的元素
    for i in include_school:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for key, value in dict.items():
        if value > max:
            max = value
            count = key
    return count

# 计算工作年限
# def calculate_work_years(resume_text):
#     # 正则表达式匹配日期和时间
#     # pattern = r"\d{4}[-/]\d{1,2}[-/]\d{1,2}"  # 2018-2022
#     pattern = r"\d{4}[.-]\d{1,2}"  # 2018.5
#     dates = re.findall(pattern, resume_text)  # 所有的时间数据
#     print(dates)
#
#     # 处理日期字符串，删除非数字和点号字符
#     dates = [re.sub(r"[^0-9.]", "", date) for date in dates]
#
#     date_objs = [datetime.strptime(date, "%Y.%m") for date in dates]
#     if not date_objs:
#         return None
#     work_years = (datetime.now() - min(date_objs, default=datetime.now())).days / 365.25
#     return work_years

# 计算工作年限
def calculate_work_years(resume_text):
    # print(resume_text)
    # 定义正则表达式模式
    pattern1 = r"\d{4}[.-]\d{1,2}-"
    pattern2 = r"\d{4}[.-]\d{1,2}"

    # 存储符合pattern1的元素的列表A
    list_A = []

    # 存储从列表A中提取的时间列表B
    list_B = []

    # 遍历字符串数组
    for item in resume_text:
        # 使用正则表达式匹配pattern1
        match1 = re.search(pattern1, item)
        if match1:
            # 将匹配到的元素添加到列表A
            list_A.append(item)

    # 遍历列表A
    for item in list_A:
        # 使用正则表达式匹配pattern2
        match2 = re.search(pattern2, item)
        if match2:
            # 将匹配到的时间添加到列表B
            list_B.append(match2.group())

    # 获取当前时间的年份
    current_year = datetime.now().year
    # print(list_A)
    # print(list_B)
    # 将时间字符串转换为年份并计算最小工作年限
    if list_B:
        years = [int(time_str[:4]) for time_str in list_B]
        min_year = min(years)
        work_years = current_year - min_year
        # print("工作年限：", work_years)
        return work_years
    else:
        print("未找到符合要求的时间元素")
        return None

# 处理工作年限和最高学历
def calculate_education_diff(work_years, education):
    education_list = ['博士', '硕士', '本科', '大专', '中专', '高中', '初中', '小学']
    education_values = [8, 7, 4, 3, 3, 3, 3, 3]
    if education in education_list:
        index = education_list.index(education)
        education_value = education_values[index]
        # print(work_years,education_value)
        diff = work_years - education_value
        return diff
    else:
        return None


