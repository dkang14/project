from neuralnet import *
import matplotlib.pyplot as plt
import numpy as np

def testNetwork1():
    '''test for functions in one variable'''
    '''using primitive methods'''
    net = Network(1,20,1)

    data = [x for x in np.arange(0,1,.001)]

    rand_data = rand.sample(data,1000)
    output = []

    i = 1
    for y in range(100):
        for x in rand_data:
            net.feedforward([x])
            net.backprop_error([math.sin(x*2*3.1415)])
            net.backprop_weight(.01,.001)
        print "Epoch iteration: " + str(i)
        i = i+1

    for x in data:
        net.feedforward([x])    
        output.append(net.output)

    plt.plot(data,output)
    plt.show()


def testNetwork2():
    '''test the projection map'''
    net = Network(2,10,2)

    data = [x for x in np.arange(0,1,.001)]
    data2 = [0 for x in np.arange(0,1,.001)]
    data5 = [rand.uniform(-1,1) for x in np.arange(0,1,.001)]
    data4 = zip(data,data)


    rand_data = rand.sample(data,len(data))
    inputs = zip(rand_data,data5)
    targets = [[x[0]**3,-x[1]**2] for x in inputs]

    net.add_dataset(inputs,targets)

    net.train(50)
        
    output1 = []
    output2 = []
    for x in data4:
        net.feedforward(x)    
        output1.append(net.output[0])
        output2.append(net.output[1])

    plt.plot(output1)
    plt.plot(output2)
    plt.show()

def testNetwork3():
    '''test the new training method'''
    net = Network(1,20,1)

    data = [x for x in np.arange(0,1,.001)]
    rand_data = rand.sample(data,len(data))

    inputs = [[x] for x in rand_data]
    targets = [[math.sin(x*10)] for x in rand_data]
    net.add_dataset(inputs,targets)

    net.train(10,.05,.0003)
    
    output = []
    for x in data:
        net.feedforward([x])    
        output.append(net.output)

    plt.plot(output)
    plt.show()

testNetwork3()
