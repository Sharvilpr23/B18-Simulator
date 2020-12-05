#include <iostream>

using namespace std;

class NAND
{
    private:
        int input_a;
        int input_b;
    public:
        NAND(){};

        NAND(int input_a, int input_b)
        :input_a(input_a), input_b(input_b){};

        bool output(){
            return !(input_a && input_b);
        };

        void input(int a, int b){
            input_a = a;
            input_b = b;
        };
};

int main(int argc, char *argv[])
{
    int j = 4;
    int k = 2;
    int m = 3;
    int n = 2;

    string filename = argv[1];



    return 0;
}