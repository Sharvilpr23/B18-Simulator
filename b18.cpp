#include <iostream>
#include <vector>
#include <utility>
#include <fstream>

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

void readInput(ifstream &fin, string filename, vector<pair<int, int>> &wiring)
{
    int pin1, pin2;
    fin.open(filename, ios::in);

    if(!fin.is_open()){
        cout << "Failure to open file\n";
        exit(1);
    }

    while(fin >> pin1 >> pin2){
        wiring.push_back(make_pair(pin1, pin2));
    };

    return;
}

int main(int argc, char *argv[])
{
    ifstream fin;
    int j = 4;
    int k = 2;
    int m = 3;
    int n = 2;
    vector<pair<int, int>> wiring;
    
    string filename = argv[1];

    readInput(fin, filename, wiring);

    for(auto pair : wiring)
    {
        cout << pair.first << " " << pair.second << "\n";
    }

    return 0;
}