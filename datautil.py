import csv
import os
import re
import numpy as np
import matplotlib.pyplot as plt
from neuralnet import *

class Dataset(object):
    def __init__(self,nodes_file, path_to_inputs,path_to_targets,startdate = 0):
        self.nodes = self.__get_nodes(nodes_file)
        self.date = 0
        self.cleaninputs = self.__extract(self.nodes,path_to_inputs,startdate)
        self.cleantargets = self.__extract(self.nodes,path_to_targets,startdate)
        assert len(self.cleaninputs) == len(self.cleantargets)
        
        self.inputs = self.process_data(self.cleaninputs)
        self.targets = self.process_data(self.cleantargets)
        
    def __get_nodes(self,nodes_file):
        upload = open(nodes_file,"rU")
        reader = csv.reader(upload)
        nodes = [str(x[0]) for x in reader]
        return nodes

    def __retrieve(self, path):
        allfiles = os.listdir(path)
        return allfiles

    def __extract(self,nodes,path,startdate):
        files = self.__retrieve(path)
        fullpath = [os.path.join(path,x) for x in files if re.search("csv",x)]
        csv_objects = [csv.reader(open(x,"rU")) for x in fullpath]
        cleandata = []
        date_index = startdate
        for x in csv_objects:
            date_index = date_index+1
            for row in x:
                if row != []:
                    for i in range(len(nodes)):
                        node = np.zeros(len(nodes))
                        node[i] = 100
                        if str(row[0]) == nodes[i]:
                            if str(row[2]) == "LMP":
                                data_entry = row
                                data_entry.append(date_index)
                                data_entry.extend(node)
                                cleandata.append([data_entry,nodes[i]])
        self.date = date_index
        return cleandata

    def process_data(self,cleandata,nodes = None):
        if nodes != None:
            pre = [x[0][3:] for x in cleandata if x[1] in nodes]
        else:
            pre = [x[0][3:] for x in cleandata]
        data = []
        for x in pre:
            data_entry = [float(y)/100. for y in x]
            data.append(data_entry)
        return data

class Output(object):
    def __init__(self,dataset,net):
        self.net = net
        self.ds = dataset
        self.nodes = dataset.nodes
        self.output = None 

    def get_output(self,nodes = None):
        if nodes == None:
            nodes = self.nodes
        data = self.ds.process_data(self.ds.cleaninputs,nodes)
        output = []
        for x in data:
            self.net.feedforward(x)
            output.append(self.net.output)
        self.output = output

    def PL_analyzer(self):
        Daily_PL = []
        for i in range(len(self.ds.inputs)):
            for j in range(24):
                input_data = self.ds.inputs[i][j]
                output_data = self.output[i][j]
                actual = self.ds.targets[i][j]
                if output_data >= input_data:
                    PL = actual - input_data
                else:
                    PL = input_data - actual
                Daily_PL.append(PL)
        Overall_PL = [0]
        for i in range(len(Daily_PL)):
            Overall_PL.append(Daily_PL[i]+Overall_PL[i])
        Overall_PL = [x*100 for x in Overall_PL]
        self.Overall_PL = Overall_PL

    def plot_PL(self):
        plt.plot(self.Overall_PL)
        plt.title("Total Profit/Loss Return over Testing Period")
        plt.xlabel("Time")
        plt.ylabel("Net Return")
        plt.show()
            
            
        
        
##### Testing ####
'''
ds = Dataset("project/Nodes.csv","project/testing/da","project/testing/rt",1)

print ds.date
'''
