# 批量复制目录下子文件夹里的文件，不包含三级目录下的文件
# 使用情景：比如在一个文件夹中，存在各个子文件夹，各个子文件夹下有各自的最新版本文件，
# 同时还有个三级目录用于存放历史版本，我们仅想复制二级目录中存放的最新版本文件汇总到一起
# 作者：小尹 时间:2021/7/21

import os
from shutil import copyfile

# 源路径
path = r'D:\Project\技术分享\Copyfiles\待复制的文件目前'
# 目标路径
out_path = r'D:\Project\技术分享\Copyfile\复制后文件'
# 记录找到的文件数量
num = 0

def copy_files(path):
    """path一最外面的目录"""
    global num
    # 遍历当前目录下的文件和子目录
    for lists in os.listdir(path):
        sub_path = path + os.path.sep + lists
        src_path = sub_path
        dst_path = out_path + os.path.sep + lists

        # 在输出文件夹中建立相应的目录
        try:
            os.mkdir(dst_path)
        except:
            pass
        # 找出子目录下的文件和第二级目录
        for sec_path in os.listdir(sub_path):
            file_path_to_test = sub_path + os.path.sep + sec_path
            # 只拷贝是文件的目录
            if os.path.isfile(file_path_to_test):
                src_file = file_path_to_test
                copyfile(src_file, dst_path + os, path.sep + sec_path)
                num += 1

def main():
    copy_files(path)
    if num >0:
        print("己有",num,"份文件被您从",path,"\n","复制到".out_path)
        print('---------------------------------------------')
        print("Congratulations! ")
    else:
        print(" Sorry!")
# Press the green button in the gutter to run the script
if __name__ == '_main_':
    main()
