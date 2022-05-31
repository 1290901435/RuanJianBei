import json
with open('data_dir/dev.json','r',encoding='utf8')as fp:    #可修改json文件
    json_data = json.load(fp)
    print('这是读取到文件数据的数据类型：', type(json_data))
    title_list= [dic["title"] for dic in json_data]
    content_list = [dic["content"] for dic in json_data]
    content_max = max(content_list, key=len, default='')
    content_min = min(content_list, key=len, default='')
    print("数据量:"+str(len(content_list)))
    print("content平均长度:"+str(len(''.join(content_list))/len(content_list)))
    print("content最大长度:"+str(len(content_max)))
    print("content最短长度:"+str(len(content_min)))

