#ifndef NEURON_H
#define NEURON_H

class Neuron
{
    public:
        /** Default constructor */
        Neuron();
        Neuron(int inputlen);
        /** Default destructor */
        virtual ~Neuron();
        /** Access inputlen
         * \return The current value of inputlen
         */
        int Getinputlen() { return inputlen; }
        /** Set inputlen
         * \param val New value to set
         */
        void Setinputlen(int val) { inputlen = val; }
        void init(int inputlen);
        void addinputs(double inputlist[], int len);
        void set_testweights();
        void set_newweights();
        void genraw();
        double get_transformed_value() {return transformed_value;}
        void set_error(double error) {this->error = error;}
        double get_error() {return error;}
        double get_weight(int n) {return weights[n];}
        void set_weight(double val, int n) {weights[n] = val;}
        double get_input(int n) { return inputs[n];}
        void set_weights(double weight,int n) {weights[n] = weight;}
        double get_bias() {return bias;}
        void set_bias(double bias) {this->bias = bias;}
        void print();
        double get_raw_value()  {return raw_value;}

    protected:

        int inputlen; //!< Member variable "inputlen"
        double * inputs; //!< Member variable "inputs"
        double * weights; //!< Member variable "weights"
        double bias; //!< Member variable "bias"
        double transformed_value; //!< Member variable "transformed_value"
        double raw_value; //!< Member variable "raw_value"
        double error; //!< Member variable "error"
    private:

};

#endif // NEURON_H
