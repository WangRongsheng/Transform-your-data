# 转化数据集格式

- yolo->voc
- voc-yolo
- voc-coco
- voc-tfrecord

# 代码解释

1. hq_file_xml.py：把文件夹下所有`.xml`文件名称写入`txt`文件；
2. see_data_shape.py：获取图片的尺寸；
3. xg_lable_images.py：批量修改同时修改图片和标签的名称；
4. voc_to_coco.py：`.xml`文件转化`.json`；
5. voc_to_coco-v2.py：`.xml`文件转化`.json`第二版；
6. voc_to_tfrecord.py：`.xml`文件转化`.tfrecord`；
7. voc_to_yolo.py：`.xml`文件转化`.txt`；
8. yolo_to_voc.py：`.txt`文件转化`.xml`；

# 参考

- https://github.com/shiyemin/voc2coco
- [数据格式转化](https://blog.csdn.net/weixin_42419002/article/details/100127714?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.compare&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.compare)
- https://blog.csdn.net/qq_38109843/article/details/90783347
