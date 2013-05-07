import sys
from neuralnet import *
from Analyzer import *

if (len(sys.argv) < 7):
    raise NameError("Not enough args")

def main(nodes_file, training_file, testing_file, numNeurons, numEpochs, learning_rate):
    nodes = get_nodes(nodes_file)
    print "Nodes to Analyze: "
    print nodes
    
    print "\nProcessing training data..."
    training_set = data_pro.gen_dataset(nodes,training_file+"/da",training_file+"/rt")
    print "Done."

    print "\nStarting Neural Net"
    net = Network(29,numNeurons,29)
    net.add_dataset(training_set[0],training_set[1])
    net.train(numEpochs, learning_rate, learning_curve = descent_learning)
    print "Training complete."

    print "\nProcessing testing data..."
    testing_set = data_pro.gen_dataset(nodes,testing_file+"/da",testing_file+"/rt")
    print "Done."

    print "\nRunning testing set"
    output = run_testing_data(testing_set[0],net)
    print "Done"

    ProfitLoss = PL_analyzer(testing_set[0],testing_set[1],output)

    plot_PL(ProfitLoss)


x = main(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]))

