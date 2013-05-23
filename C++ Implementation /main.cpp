#include <iostream>
#include "Network.h"
using namespace std;

int main()
{
    int dataset_len = 4;
    int input_len =2;
    int output_len = 2;
    double inputdata[] = {0,0,0,1,1,0,1,1};
    double target[] ={1,0,1,0,1,0,0,1};
    Network * net = new Network(input_len, 4, output_len);
    net->add_dataset(inputdata, dataset_len, target, dataset_len);
    net->train(100,0.2,true);
    net->printoutput(inputdata, dataset_len, target,dataset_len);
    return 0;
}