import os
from xml.dom.minidom import Document

def find_txt(dir_path):
    list1=[]
    str1=''
    for root,dirs,files in os.walk(dir_path):
        for name in files :
            if (name.endswith('.txt')):
                list1.append(os.path.join(root,name))
    return list1

def get_YoloInfo(txt_dir):
    f=open(txt_dir,'r')
    line_info = f.readlines()
    L=len(line_info)
    label_classes=[]
    for line in range(L):
        label_classes.append('x')
        line_info[line]=line_info[line].strip()
        each_data = line_info[line].split(' ')
        classes = int(each_data[0])
        x_center = float(each_data[1])
        y_center = float(each_data[2])
        width_nor = float(each_data[3])
        height_nor = float(each_data[4])
        label_classes[line]=[classes,x_center,y_center,width_nor,height_nor]
    return label_classes

def Yolo_voc_data(YoloInfo):
    #修改label类别
    label_list=['mask','no-mask']
    num = len(YoloInfo)
    #修改图片数据
    width=416
    height=416
    voc_data=[]
    for each in range(num):
        voc_data.append('x')
        classes = label_list[YoloInfo[each][0]]
        x_center = YoloInfo[each][1]*width
        y_center = YoloInfo[each][2]*height
        width_nor = YoloInfo[each][3]*width
        height_nor = YoloInfo[each][4]*height

        voc_xmin = str(int(x_center - (width_nor/ 2)))
        voc_ymin = str(int(y_center - (height_nor / 2)))
        voc_xmax = str(int(x_center + (width_nor / 2)))
        voc_ymax = str(int(y_center + (height_nor / 2)))

        voc_data[each]=[classes,voc_xmin,voc_ymin,voc_xmax,voc_ymax]
    return voc_data

##dir_路径修改为 YOLO标签txt存放的地方
dir_= find_txt('train\\labels\\')
mk_dir = 'train/annotation/'
if os.path.exists(mk_dir)==False:
    os.mkdir(mk_dir)

for each_file in dir_:
    folder_txt=each_file.split('\\')[-1]  # 根据dir_路径调整
    file_name = each_file.split('\\')[-1]  # 根据dir_路径调整
    path_txt = each_file
    print(folder_txt)
    width = '416'   #修改图片数据
    height ='416'    #修改图片数据
    depth = '3'    #修改图片数据
    info_1 = get_YoloInfo(each_file)
    info_voc = Yolo_voc_data(info_1)
    
    doc=Document()
    annotation=doc.createElement('annotation')

    doc.appendChild(annotation)
    
    folder = doc.createElement('folder')
    folder_txt = doc.createTextNode(folder_txt)
    folder.appendChild(folder_txt)
    annotation.appendChild(folder)

    filename = doc.createElement('filename')
    filename_txt = doc.createTextNode(file_name)
    filename.appendChild(filename_txt)
    annotation.appendChild(filename)

    path = doc.createElement('path')
    path_txt = doc.createTextNode(path_txt)
    path.appendChild(path_txt)
    annotation.appendChild(path)

    source = doc.createElement('source')
    annotation.appendChild(source)

    database=doc.createElement('database')
    database_txt=doc.createTextNode('Unknown')
    database.appendChild(database_txt)
    source.appendChild(database)

    size = doc.createElement('size')
    annotation.appendChild(size)

    width = doc.createElement('width')
    width_txt = doc.createTextNode('416')   #修改图片数据
    width.appendChild(width_txt)
    size.appendChild(width)

    height = doc.createElement('height')
    height_txt = doc.createTextNode('416')   #修改图片数据 
    height.appendChild(height_txt)
    size.appendChild(height)

    depth = doc.createElement('depth')
    depth_txt = doc.createTextNode('3')   #修改图片数据
    depth.appendChild(depth_txt)
    size.appendChild(depth)

    segmented = doc.createElement('segmented')
    segmented_txt = doc.createTextNode('0')
    segmented.appendChild(segmented_txt)
    annotation.appendChild(folder)
    object1=[]
    for i in range(len(info_voc)):
        object1.append('name'+str(i))
        object1[i]= doc.createElement('object')
        annotation.appendChild(object1[i])

        name = doc.createElement('name')
        name_txt = doc.createTextNode(info_voc[i][0])
        name.appendChild(name_txt)
        object1[i].appendChild(name)

        pose = doc.createElement('pose')
        pose_txt = doc.createTextNode('Unspecified')
        pose.appendChild(pose_txt)
        object1[i].appendChild(pose)

        truncated = doc.createElement('truncated')
        truncated_txt = doc.createTextNode('0')
        truncated.appendChild(truncated_txt)
        object1[i].appendChild(truncated)

        difficult = doc.createElement('difficult')
        difficult_txt = doc.createTextNode('0')
        difficult.appendChild(difficult_txt)
        object1[i].appendChild(difficult)

        bndbox = doc.createElement('bndbox')
        object1[i].appendChild(bndbox)

        xmin = doc.createElement('xmin')
        xmin_txt = doc.createTextNode(info_voc[i][1])
        xmin.appendChild(xmin_txt)
        bndbox.appendChild(xmin)

        ymin = doc.createElement('ymin')
        ymin_txt = doc.createTextNode(info_voc[i][2])
        ymin.appendChild(ymin_txt)
        bndbox.appendChild(ymin)

        xmax = doc.createElement('xmax')
        xmax_txt = doc.createTextNode(info_voc[i][3])
        xmax.appendChild(xmax_txt)
        bndbox.appendChild(xmax)

        ymax = doc.createElement('ymax')
        ymax_txt = doc.createTextNode(info_voc[i][4])
        ymax.appendChild(ymax_txt)
        bndbox.appendChild(ymax)
    dirrr='train/annotation/'+file_name[:-4]+'.xml'    # 改变VOC标签xml文件存放地点
    print(dirrr)
    f=open(dirrr,'w')
    doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')
    f.close()
   











