#include <iostream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>

using namespace std;

/**
*	compares two vector lengths
*/
template<class T>
void comp(vector<T> v1, vector<T> v2){
	if(v1.size() != v2.size()){
		cout << "vectors not the same size\n";
		exit(1);
	}
}

/**
*	Calculates Jaccard index between two vectors
*/
template<class T>
double jaccard(vector<T> v1, vector<T> v2){
	comp(v1, v2);
	int f11 = 0, f00 = 0;
	for (unsigned int i=0; i < v1.size(); i++){
		if(v1[i] == v2[i]){
			if((int)v1[i] - 48)//parse char to int
				f11++;
			else
				f00++;
		}
	}
	cout << f11 << "," << f00 << '\n';
	return double(f11) / double(v1.size() - f00);
}

int main(int argc, char* argv[]){
	
	//Reads the matrix file
	int numRows = atoi(argv[1]);
        int numColumns = atoi(argv[2]);
        vector<vector<char> > data(numRows);
        string row;
        ifstream file("matrix.txt");
        for (int i = 0; i < numRows; ++i){
                getline(file,row);
                data[i].resize(numColumns);
                istringstream iss(row);
                int j=0;
                while(iss){
                        iss >> data[i][j];
                        j++;
                }
        }
	cout << "Genes matrix saved\n";
		
	//Calculates similarity matrix
	for (int i = 0; i < numRows; i++) {
    		for (int j = 0; j < numRows; j++) {
                        //printf("%f\n",jaccard(data[i],data[j]));
        		cout << jaccard(data[i], data[j]);
			cout << "\t";
    		}
		cout << "\n";
	}
}
