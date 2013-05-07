from neuralnet import *
import data_processing_util as data_pro
import csv
import matplotlib.pyplot as plt

def get_nodes(nodes_file):
    upload = open(nodes_file,"rU")
    reader = csv.reader(upload)
    nodes = [str(x[0]) for x in reader]
    return nodes

def run_testing_data(dataset,net):
    output = []
    for x in dataset:
        net.feedforward(x)
        output.append(net.output)
    return output


def PL_analyzer(testing_set, validate_set,output):
    Daily_PL = []
    for i in range(len(testing_set)):
        for j in range(24):
            input_data = testing_set[i][j]
            output_data = output[i][j]
            actual = validate_set[i][j]
            if output_data >= input_data:
                PL = actual - input_data
            else:
                PL = input_data - actual
            Daily_PL.append(PL)
    Overall_PL = [0]
    for i in range(len(Daily_PL)):
        Overall_PL.append(Daily_PL[i]+Overall_PL[i])
    Overall_PL = [x*100 for x in Overall_PL]
    return Overall_PL 

def plot_PL(Overall_PL):
    plt.plot(Overall_PL)
    plt.title("Total Profit/Loss Return over Testing Period")
    plt.xlabel("Time")
    plt.ylabel("Net Return")
    plt.show()
    
