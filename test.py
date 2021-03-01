import os

def get_uploaded_images():
    rootdir = os.getcwd()
    print(rootdir)
    filenames = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            filenames.append(file)
    return filenames

filenames = get_uploaded_images()

def printdir():
    for filename in filenames:
        print(filename)

if __name__ == '__main__':
    printdir()