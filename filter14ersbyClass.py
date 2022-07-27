def filter14ers(merged_14ers, class_limit):

    class_dict = {'Easy Class 3':2.5,'Difficult Class 2':2.5, 'Class 2':2, 'Class 1':1, 'Class 3':3,'Class 4':4}

    t = 0
    class_num = []
    while t < len(merged_14ers.index):
        class_num.append(class_dict[merged_14ers['class_num'][t]])
        t+=1

    merged_14ers['class_num'] = class_num

    limited_df = merged_14ers[(merged_14ers['class_num'].astype(float)<=class_limit)]
    return limited_df