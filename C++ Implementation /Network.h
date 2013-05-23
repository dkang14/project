#ifndef NETWORK_H
#define NETWORK_H

#include "Neuron.h"
#include "HiddenNeuron.h"
#include "OutputNeuron.h"


class Network
{
    public:
        /** Default constructor */
        Network(int num_inputlayer, int num_hiddenlayer, int num_outputlayer);
        /** Default destructor */
        virtual ~Network();
        void add_dataset(double input_dataset[], int input_dataset_len, double target_dataset[], int target_dataset_len);
        void print();
        void printoutput(double input_dataset[], int input_dataset_len, double target_dataset[], int target_dataset_len);
        void train(int num_iteration, double learning_rate, bool decent_learning);
    protected:
    private:
        HiddenNeuron * hiddenlayer; //!<pointer to an array of neuron in hiddenlayer
        OutputNeuron * outputlayer; //!< pointer to an array of outputlayer
        int num_inputlayer;
        int num_hiddenlayer;
        int num_outputlayer;
        double * hidden_output;
        double * output; //!< pointer to output array

        double ** input_array; //!<pointer to input data array set
        int inputset_len; //!< input data set length
        double ** target_array; //!< pointer to target deta array set
        int targetset_len; //!< target data length
        int outputlen; //!< output data length


        void feedforward(double* inputlist, int inputlist_len);
        void backprop_error(double* targetlist, int targetlist_len);
        void backprop_weight(double learning_rate);
        void train_one_iteration(double learning_rate);



};


#endif // NETWORK_H
