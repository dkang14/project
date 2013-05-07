import csv
import os
import re
import numpy as np


def retrieve(path):
    allfiles = os.listdir(path)
    return allfiles

def extract(nodes,path):
    files = retrieve(path)
    fullpath = [os.path.join(path,x) for x in files if re.search("csv",x)]
    csv_objects = [csv.reader(open(x,"rU")) for x in fullpath]
    data = []
    date_index = 1
    for x in csv_objects:
        for row in x:
            if row != []:
                for i in range(len(nodes)):
                    node = np.zeros(len(nodes))
                    node[i] = 100
                    if str(row[0]) == nodes[i]:
                        if str(row[2]) == "LMP":
                            data_entry = row[3:]
                            data_entry.append(date_index)
                            data_entry.extend(node)
                            data_entry = [float(x)/100. for x in data_entry]
                            data.append(data_entry)
        date_index = date_index+1
    return data

def gen_dataset(nodes,input_path,target_path):
    inputs = extract(nodes,input_path)
    targets = extract(nodes,target_path)
    return (inputs,targets)

