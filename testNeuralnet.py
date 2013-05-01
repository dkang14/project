from neuralnet import *
import matplotlib.pyplot as plt
import numpy as np
from stocastic_functions import normal



def testNetwork2():
    '''test the projection map'''
    net = Network(4,5,1)

    data = [x for x in np.arange(-1,1,.001)]
    data2 = [0 for x in np.arange(0,1,.001)]
    data5 = [rand.uniform(-1,1) for x in np.arange(0,1,.001)]
    data4 = zip(data,data,data,data)


    rand_data = rand.sample(data,len(data))
    inputs = zip(rand_data,rand_data,rand_data,rand_data)
    targets = [[x[0]**2] for x in inputs]

    net.add_dataset(inputs,targets)

    net.train(3,.1)
        
    output1 = []
    for x in data4:
        net.feedforward(x)    
        output1.append(net.output)

    plt.plot(data,output1)
    plt.show()

def testNetwork3():
    '''test the new training method'''
    net = Network(1,20,1)
    print net.hiddenlayer[0].bias
    print net.hiddenlayer[0].weights
    
    data = [x for x in np.arange(-1,1,.01)]
    rand_data = rand.sample(data,len(data))

    inputs = [[x] for x in rand_data]
    targets = [[math.sin(x*5)] for x in rand_data]
    net.add_dataset(inputs,targets)

    net.feedforward([1])
    print net.hiddenlayer[0].raw_value
    print net.hiddenlayer[0].transformed_value

    net.train(20,0.1)
    
    output = []
    for x in data:
        net.feedforward([x])    
        output.append(net.output)
    dataout = [math.sin(x*5) for x in data]
    plt.plot(data,dataout,"b")
    plt.plot(data,output,"r")
    plt.show()

def stocastic():
    '''test model under stocastic functions'''

    net = Network(1,200,1)
    price = normal(1000,.5,0,.01)
    time = [x/1000. for x in range(1000)]
    data = zip(time,price)
    
    rand_data = rand.sample(data,len(data))
    inputs = [[x[0]] for x in rand_data]
    targets = [[x[1]] for x in rand_data]

    net.add_dataset(inputs,targets)

    net.train(150,.01)

    output = []
    for x in price:
        net.feedforward([x])    
        output.append(net.output)


    plt.plot(time,price, 'b')
    plt.plot(time,output, 'r')
    plt.show()        

def clusters():
    '''pre-process cluster data'''
    f = open("5clusters.txt")
    data = [x.strip().rsplit(" ") for x in f]
    data = data[1:]
    rand_data = rand.sample(data,len(data))

    training_raw = rand_data[0:450]
    testing_raw = rand_data[450:]
    inputs = [(int(x[0])/100.,int(x[1])/100.) for x in training_raw]
    targets = [[int(x[2])] for x in training_raw]
    testing = [(int(x[0])/100.,int(x[1])/100.) for x in testing_raw]
    correct_ans = [int(x[2]) for x in testing_raw]

    '''test on network'''
    net = Network(2,15,1)
    net.add_dataset(inputs,targets)
    net.train(50,.08,descent_learning)

    output = []
    for x in testing:
        net.feedforward(x)
        output.append(net.output)
    output = [int(round(x[0])) for x in output]
    numcorrect = 0
    for i in range(len(output)):
        result = False
        if output[i] == correct_ans[i]:
            numcorrect = numcorrect + 1
            result = True
        print "NN output: " + str(output[i]) + " Actual: " + str(correct_ans[i]) + " " +str(result)
    print "Number Correct: " + str(numcorrect) + " / " + str(len(correct_ans))

    x_training = [t[0] for t in inputs]
    y_training = [t[1] for t in inputs]

    x_testing = [t[0] for t in testing]
    y_testing = [t[1] for t in testing]
    '''
    plt.plot(x_training,y_training, "o")
    plt.show()
    plt.plot(x_testing, y_testing, "o")
    plt.show()
'''
clusters()
