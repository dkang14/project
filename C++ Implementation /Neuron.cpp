#include "Neuron.h"
#include <stdlib.h>

#include <iostream>

using namespace std;

Neuron::Neuron()
{
    this->inputlen = 0;//ctor
    this ->inputs = NULL;
    this->weights = NULL;
}

Neuron::Neuron(int inputlen)
{
    this->inputlen = inputlen;//ctor
    this ->inputs = NULL;
}

Neuron::~Neuron()
{
    //dtor
}

void Neuron::init(int inputlen)
{
    this->inputlen = inputlen;//ctor
    this->inputs = new double[inputlen];
    this->weights = new double[inputlen];
    this->bias = 0.5;
    this->raw_value = 0.0;
    this->transformed_value = 0.0;
}

void Neuron::addinputs(double inputlist[], int len)
{
    //todo
    /*
    if len(inputlist) == self.inputlen:
            self.inputs = inputlist
        else:
            raise NameError('InputLen_Mismatch')
     */
     if(len != inputlen)
     {
         cout<<"input length not match!"<<endl;//print error message and
         return;

     }
     for(int i = 0; i<inputlen; i++)
     {
         inputs[i] = inputlist[i];
     }
}

void Neuron::set_testweights()
{
    // self.weights = [.5 for x in range(self.inputlen)]
    for(int i = 0; i<inputlen; i++)
     {
         weights[i] = 0.5;
     }
}

void Neuron::set_newweights()
{
    /*
     '''Set initial weights here'''
        self.weights = [rand.uniform(-1,1) for x in range(self.inputlen)]
    */
     for(int i = 0; i<inputlen; i++)
     {
         weights[i] = 1.0 - 2*((double)rand())/RAND_MAX;
     }
}

void Neuron::print()
{
     cout<<"inputs-weights :";
     for(int i = 0; i<inputlen; i++)
     {
         cout<<inputs[i]<<"-"<<weights[i]<<"; ";
     }
     cout<<endl;
     cout<<"bias:"<<bias<<"; rawval:"<<raw_value<<"; transformed:"<<transformed_value<<"; error:"<<error<<endl;
}

void Neuron::genraw()
{
    /*
    dot = [self.inputs[x]*self.weights[x]
                          for x in range(self.inputlen)]
        self.raw_value = 0
        for x in dot:
            self.raw_value = self.raw_value + x
    */
    double sum = 0;
    for(int i = 0; i< inputlen; i++)
    {
        sum = sum + inputs[i] * weights[i];
    }
    raw_value = sum;
}



