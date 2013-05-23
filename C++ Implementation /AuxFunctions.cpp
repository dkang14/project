#include <math.h>
double const_learning(double x)
{
    return 1.0;
}

double decent_learning(double x)
{
    if(x < 0.1) return 1.0;
    return 1.5 - x;
}


double safeExp(double x)
{
    if(x > 500) return exp(500);
    if(x < -500) return exp(-500);
    return exp(x);
}


double sigmoid(double x)
{
    return 1.0/(1.0+safeExp(-x*10));
}



double sigmoidPrime(double x)
{
    double tmp = sigmoid(x);
    return tmp * (1-tmp);
}
