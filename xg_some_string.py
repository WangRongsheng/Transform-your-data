import os

def revise(path):
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    for filename in files:
        try:
            file_path = os.path.join(path, filename) 
            print(filename)
            file_path1 = os.path.join(path, filename.replace('.rf.','_'))
            os.rename(file_path,file_path1)
        except:
            continue  
 
revise('images/') #需要更改的文件夹所在路径
