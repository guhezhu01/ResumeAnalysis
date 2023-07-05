from ecloud import CMSSEcloudOcrClient
import json
from docx import Document
from common.utils import *
import base64



accesskey = '2456ff44b570493dacf18b8f0082b2ea'
secretkey = 'a23d404e53c04929825d4e86e4c179cd'
url = 'https://api-wuxi-1.cmecloud.cn:8443'

id = 1
resume_image_path = f'../../dataset_CV/base64/images/{id}_01.png'


def request_smartstructure_file(image_path):
    print("请求智能结构化接口")
    requesturl = '/api/ocr/v1/smartstructure'
    imagepath = image_path
    response_dict = None
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_file(requestpath=requesturl, imagepath= imagepath)
        response_dict = json.loads(response.text)
        if response_dict:
            print("接口请求成功")
        # print(response_dict)

    except ValueError as e:
        print(e)
    return response_dict

def request_webimage_file(image_path):
    print("请求网络图片文字接口")
    requesturl = '/api/ocr/v1/webimage'
    imagepath = image_path
    response_dict = None
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_file(requestpath=requesturl, imagepath= imagepath)
        response_dict = json.loads(response.text)
        if response_dict:
            print("接口请求成功")
        # print(response_dict)
        
    except ValueError as e:
        print(e)
    return response_dict

def request_webimage_base64(resume_base):
    # imagepath = 'D:\\JG-CMSS\\PaaS_MrZ\\智库2023\\SDK\\PythonSDK\\Python_SDK\\test_code\\sfz.jpg'
    # requesturl = '/api/ocr/v1/webimage'
    # with open(imagepath, 'rb') as f:
    #     img = f.read()
    requesturl = '/api/ocr/v1/webimage'
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_base64(requestpath=requesturl, base64=resume_base)
        print(response.text)
    except ValueError as e:
        print(e)


def request_webimage_url():
    print("请求URL参数")
    requesturl = '/api/ocr/v1/webimage'
    imageurl = 'http://10.253.51.155:10086/wangluotupian.jpg'
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_url(requesturl, imageurl)
        print(response.text)
    except ValueError as e:
        print(e)

def request_handwriting():
    requesturl = '/api/ocr/v1/handwriting'
    imagepath = './webimage.jpg'
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_file(requestpath=requesturl, imagepath= imagepath)
        print(response.text)
    except ValueError as e:
        print(e)

def request_customverify():
    requesturl = '/api/ocr/v1/selfdefinition'
    imagepath = './shenfenzheng.jpg'
    options = {}
    options['TemplateId'] = '76542407608369152'
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_file(requestpath=requesturl, imagepath= imagepath, options=options)
        print(response.text)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    request_smartstructure_file(resume_image_path)
    request_webimage_file(resume_image_path)
    # request_webimage_base64(resume_base)
    # request_webimage_url()
    #request_handwriting()
    #request_customverify()

