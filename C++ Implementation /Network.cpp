#include "Network.h"
#include "HiddenNeuron.h"
#include "OutputNeuron.h"
#include <iostream>
#include "AuxFunctions.h"


using namespace std;

Network::Network(int num_inputlayer, int num_hiddenlayer, int num_outputlayer)
{
    //ctor
    /* """initiate # of Neurons per layer"""
    def __init__(self,inputlayer,hiddenlayer,outputlayer):
        self.hiddenlayer = self.addNeurons(inputlayer,hiddenlayer,HiddenNeuron)
        self.outputlayer = self.addNeurons(hiddenlayer,outputlayer,OutputNeuron)
        self.input = None
        self.target = None
        self.output = None
    */
    this->num_inputlayer = num_inputlayer;
    this->num_hiddenlayer = num_hiddenlayer;
    this->num_outputlayer = num_outputlayer;
    outputlayer = new OutputNeuron[num_outputlayer];
    for(int i = 0; i< num_outputlayer; i++)
    {
        outputlayer[i].init(num_hiddenlayer);
        outputlayer[i].Setinputlen(num_hiddenlayer);
        outputlayer[i].set_newweights();
    }
    output = new double[num_outputlayer];

    hiddenlayer = new HiddenNeuron[num_hiddenlayer];
    for(int i = 0; i< num_hiddenlayer; i++)
    {
        hiddenlayer[i].init(num_inputlayer);
        hiddenlayer[i].Setinputlen(num_inputlayer);
        hiddenlayer[i].set_newweights();
    }
    hidden_output = new double[num_hiddenlayer];


}

Network::~Network()
{
    //dtor
}

void Network::add_dataset(double input_dataset[], int input_dataset_len, double target_dataset[], int target_dataset_len)
{
    inputset_len = input_dataset_len;
    input_array = new double*[inputset_len];
    for(int i = 0; i<input_dataset_len; i++)
    {
        input_array[i] = new double[num_inputlayer];
        for(int j = 0; j<num_inputlayer; j++)
        {
            input_array[i][j]= input_dataset[i*num_inputlayer+j];
        }
    }
    targetset_len = target_dataset_len;
    target_array = new double * [targetset_len];
    for(int i = 0; i<target_dataset_len; i++)
    {

         target_array[i] = new double[num_outputlayer];
         for(int j = 0; j<num_outputlayer; j++)
        {
            target_array[i][j]= target_dataset[i*num_outputlayer+j];
        }
    }

}

void Network::feedforward(double* inputlist, int inputlist_len)
{
    /*
      def feedforward(self, inputlist):
        """computes an output given an input, given current set of weights"""

    */


    double* hidden_output = new double[num_hiddenlayer];
    for(int i = 0; i<num_hiddenlayer; i++)
    {
        hiddenlayer[i].addinputs(inputlist, num_inputlayer);
        hiddenlayer[i].genraw();
        hiddenlayer[i].activate();
        hidden_output[i] = hiddenlayer[i].get_transformed_value();
    }
    for(int i = 0; i<num_outputlayer; i++)
    {
        outputlayer[i].addinputs(hidden_output, num_hiddenlayer);
        outputlayer[i].genraw();
        outputlayer[i].activate();
        output[i] = outputlayer[i].get_transformed_value();
    }
}

void  Network::backprop_error(double* targetlist, int targetlist_len)
{
   /*
    def backprop_error(self,targetlist):
        '''For each node, calculate the error using backpropagation as explained by wikipedia'''

   */
   for(int i = 0; i<num_outputlayer; i++)
   {
       double err = outputlayer[i].get_transformed_value() - targetlist[i];
       outputlayer[i].set_error(err);
   }
   for(int i = 0; i< num_hiddenlayer;i++)
   {
       double err = 0;
       for(int j = 0; j< num_outputlayer; j++)
       {
           err = err + outputlayer[j].get_weight(i) * outputlayer[j].get_error();
       }
       err = err * sigmoidPrime(hiddenlayer[i].get_raw_value());
       hiddenlayer[i].set_error(err);
   }
}

void Network::backprop_weight(double learning_rate)
{
    for(int i=0; i<num_outputlayer; i++)
    {
        for(int j=0; j<outputlayer[i].Getinputlen();j++)
        {
            double delta = outputlayer[i].get_error() * outputlayer[i].get_input(j);
            double weights = -learning_rate * delta + outputlayer[i].get_weight(j);
            outputlayer[i].set_weights(weights, j);
        }
    }
    for(int i=0; i<num_hiddenlayer;i++)
    {
        for(int j=0; j<hiddenlayer[i].Getinputlen();j++)
        {
            double delta = hiddenlayer[i].get_error() * hiddenlayer[i].get_input(j);
            double weights = -learning_rate * delta + hiddenlayer[i].get_weight(j);
            hiddenlayer[i].set_weights(weights,j);
        }
        double bias = -learning_rate * hiddenlayer[i].get_error() + hiddenlayer[i].get_bias();
        hiddenlayer[i].set_bias(bias);
    }
}

void Network::train_one_iteration(double learning_rate)
{
    for(int i=0; i<inputset_len;i++)
    {
/*
        cout<<"input:";
        for(int j=0; j<num_inputlayer;j++)
        {
            cout<<input_array[i][j]<<"  ";
        }
        cout<<endl;
*/
        feedforward(input_array[i],num_inputlayer);
/*
        cout<<"output: ";
        for(int j=0; j<num_outputlayer;j++)
        {
            cout<<output[j]<<"  ";
        }
        cout<<endl;
        cout<<"target: ";

        for(int j=0; j<num_outputlayer;j++)
        {
            cout<<target_array[i][j]<<"  ";
        }
        cout<<endl;
*/
        backprop_error(target_array[i],num_outputlayer);
        backprop_weight(learning_rate);
    }
}

void Network::train(int num_iteration, double learning_rate, bool decent_learn)
{
    std::cout<<"learning"<<endl;
    double adjusted_learning_rate;
    for(int i=0;i<num_iteration;i++)
    {
        double iter_frac = ((double)i)/num_iteration;
        if (decent_learn == true)
        {
            adjusted_learning_rate = learning_rate * decent_learning(iter_frac);
        }
        else
        {
            adjusted_learning_rate = learning_rate * const_learning(iter_frac);
        }
    train_one_iteration(adjusted_learning_rate);
    std::cout<<"Epoch iteration:"<<i+1<<endl;
    }
    cout<<"done"<<endl;
}

void Network::print()
{
    cout<<"outputlayer"<<endl;
     for(int i =0; i< num_outputlayer; i++)
    {
        outputlayer[i].print();
    }
    cout<<endl;
    cout<<"hiddenlayer"<<endl;
    for(int i =0; i< num_hiddenlayer; i++)
    {
        hiddenlayer[i].print();
    }
    cout<<endl;

}

void Network::printoutput(double input_dataset[], int input_dataset_len, double target_dataset[], int target_dataset_len)
{
    add_dataset(input_dataset, input_dataset_len,target_dataset,target_dataset_len);

    for(int i=0; i<input_dataset_len; i++)
    {
        feedforward(input_array[i],num_inputlayer);
        for(int j=0;j<num_outputlayer;j++)
        {
            cout<<"data "<<i<<": ";
            cout<<"output"<<j<<":"<<output[j]<<", target"<<j<<": "<<target_array[i][j]<<endl;
        }
        cout<<endl;

    }
}
