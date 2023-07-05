from data_handing import datahanding

id = 34

image_path = f'dataset_CV/base64/images/{id}_01.png'
def analyze(imagepath):
    resume_data = datahanding(imagepath)
    # print(resume_data)
    return resume_data

if __name__ == "__main__":
    analyze(image_path)
