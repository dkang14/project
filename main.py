import sys
from neuralnet import *
import datautil

if (len(sys.argv) < 7):
    raise NameError("Not enough args")

def main(nodes_file, training_file, testing_file, numNeurons, numEpochs, learning_rate):
    print "Processing training data..."
    training_set = datautil.Dataset(nodes_file,training_file+"/da",training_file+"/rt")
    print "Done."

    print "\nStarting Neural Net"
    net = Network(29,numNeurons,29)
    net.add_dataset(training_set.inputs,training_set.targets)
    net.train(numEpochs, learning_rate, learning_curve = descent_learning)
    print "Training complete."

    print "\nProcessing testing data..."
    testing_set = datautil.Dataset(nodes_file,testing_file+"/da",testing_file+"/rt")
    print "Done."

    print "\nRunning testing set..."
    output = datautil.Output(testing_set,net)
    output.get_output()
    print "Done"

    output.PL_analyzer()
    output.plot_PL()


x = main(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]))

