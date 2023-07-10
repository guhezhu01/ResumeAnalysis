import re
from datetime import datetime
from docx import Document
from io import BytesIO
from PIL import Image
from docx2pdf import convert
from pdf2image import convert_from_path
import base64
import os


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
    # print(dict)
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
    pattern2 = r"[12]\d{3}-"
    pattern3 = r'[12]\d{3}'

    # 存储符合pattern1的元素的列表A
    list_A = []

    # 存储从列表A中提取的时间列表B
    list_B = []

    # 遍历字符串数组
    for item in resume_text:
        # 使用正则表达式匹配pattern1
        match1 = re.search(pattern1 + '|' + pattern2, item)
        if match1:
            # 将匹配到的元素添加到列表A
            list_A.append(item)

    # 遍历列表A
    for item in list_A:
        # 使用正则表达式匹配pattern2
        match2 = re.search(pattern3, item)
        if match2:
            # 将匹配到的时间添加到列表B
            list_B.extend(re.findall(pattern3, item))

    # 获取当前时间的年份
    print(f"字符串数组列表：{list_A}，时间列表：{list_B}")
    current_year = datetime.now().year
    # print(list_A)
    # print(list_B)
    # 将时间字符串转换为年份并计算最小工作年限
    if list_B:
        years = [int(time_str[:4]) for time_str in list_B]
        min_year = min(years)
        work_years = current_year - min_year
        print("最大时间与最小时间的差：", work_years)
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
        print(f"work_years={work_years},education_value={education_value}")
        return diff
    else:
        return None


def preProcess(pattern):
    dist = [len(pattern) + 1] * 128
    for i in range(len(pattern)):
        dist[ord(pattern[i])] = len(pattern) - i
    return dist


def zhusunday(T, P, pos):
    # T是长文本串，P是要匹配的短字符串，pos是T中下标开始的位置
    Tindex = pos + len(P) - 1  # Tindex是在T中搜索的当前位置，采用从右向左探索
    pindex = len(P) - 1
    pipeipos = 0
    pipeicishu = 0
    dist = preProcess(T)
    print(dist)

    while Tindex < len(T):  # 遍历源串T
        pipeicishu += 1
        # 2种情况: 1和2
        if T[Tindex] != P[pindex]:  # 1：不匹配模式串P最后一个字符
            # 有2种情况 ，分别是1A和1B
            if dist[T[Tindex]] == len(P):  # A：目标字符不在模式串中，是坏字符,dist是模式串预处理数组，对0—127的ASCII字符能使模式窗口向右移动距离进行了预先统计。
                if T[Tindex + 1] != P[0]:  # 多验证坏字符左侧的一个字符
                    Tindex += len(P) + 1  # 跳跃模式串长度个字符探索，验证成功比坏字符多跳一个
                else:
                    Tindex += len(P)  # 验证不成功，跳跃模式串长度个字符
            else:  # B：改进处:目标字符在模式串中，但不是模式串最后一个字符
                x = len(P) - 2 - dist[T[Tindex]]  # x是由右向左第一次不匹配时字符的下标 ，因为没有全匹配，其值不能小于0
                if P[x] != T[Tindex - 1] and x >= 0:
                    Tindex += dist[T[Tindex]] + 1
                else:  # 这种情况多数不成立
                    Tindex += dist[T[Tindex]]
        else:  # 2：匹配模式串的最后一个字符，回溯追查，对应 2种情况 ，分别是 2C和2D
            pipeipos = quanpipei(T, P, Tindex, len(P) - 1)  # 从最后一个字符向前进行匹配
            if pipeipos != 0:  # 2C：由后向前部分字符匹配，没有全匹配，这里也对 Sunday进行了改进
                x = len(P) - 2 - dist[T[Tindex]]  # x是由右向左最后一次匹配的字符左侧的字符的下标，因为没有全匹配，其值不能小于0
                if P[x] != T[Tindex - 1] and x >= 0:
                    Tindex += dist[T[Tindex]] + 1  # 多移动
                else:
                    Tindex += dist[T[Tindex]]
            else:  # 2D：所有字符全匹配
                return Tindex - len(P) + 1  # 返回匹配的起始下标

    if Tindex >= len(T):  # 匹配结束，依然没有返回，表示未匹配成功
        return -1


T = "abcoefcacdxdbcd"
P = "dbcd"
pos = 0


# print(zhusunday(T,P,pos))


# sunday 算法，T 为文本串，p 为模式串
def sunday(T: str, p: str) -> int:
    n, m = len(T), len(p)

    bc_table = generateBadCharTable(p)  # 生成后移位数表

    i = 0
    while i <= n - m:
        j = 0
        if T[i: i + m] == p:
            return i  # 匹配完成，返回模式串 p 在文本串 T 的位置
        if i + m >= n:
            return -1
        i += bc_table.get(T[i + m], m + 1)  # 通过后移位数表，向右进行进行快速移动
    return -1  # 匹配失败


# 生成后移位数表
# bc_table[bad_char] 表示遇到坏字符可以向右移动的距离
def generateBadCharTable(p: str):
    m = len(p)
    bc_table = dict()

    for i in range(m):  # 迭代到最后一个位置 m - 1
        bc_table[p[i]] = m - i  # 更新遇到坏字符可向右移动的距离
    return bc_table


print(sunday("abbcfdddbddcaddebc", "aaaaa"))
print(sunday("abbcfdddbddcaddebc", "bcf"))
