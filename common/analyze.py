from data_handing import datahanding

imagepath = 'dataset_CV/base64/15_01.png'
def analyze(imagepath):
    resume_data = datahanding(imagepath)
    print(resume_data)
    return resume_data


if __name__ == "__main__":
    analyze(imagepath)
