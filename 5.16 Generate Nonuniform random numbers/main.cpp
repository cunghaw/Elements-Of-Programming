#include <iostream>
#include <random>
#include <vector>
#include <exception>
#include <map>

using namespace std;

int generateNonUniformDistribution( vector<int>& arr_vec, vector<double>& prob_vec ) {
	random_device rd; 
	mt19937 generator(rd());
	uniform_real_distribution<double> distribution(0, 1);
	double p = distribution(generator);
	vector<double>::iterator it;
	for ( it = prob_vec.begin(); it!= prob_vec.end(); it++ ) {
		if ( p <= *it )
			return arr_vec[ distance( prob_vec.begin(), it ) ];
	}	
	
	return arr_vec.back();
}

int main() {
	int arr[] = { 3, 5, 7, 11 };
	vector<int> arr_vec(arr, arr + sizeof( arr ) / sizeof( int ));
	double prob_arr[] = { 0.5, 0.33, 0.11, 0.05 };
	vector<double> prob_vec( prob_arr, prob_arr + sizeof( prob_arr ) / sizeof( double ) );
	vector<double>::iterator it;	
	double a_prob = 0;
	for ( it = prob_vec.begin(); it!= prob_vec.end(); it++ ) {
		a_prob = a_prob + *it;
		*it = a_prob;
	}
	
	map<int, int> result;
	for ( int i = 0; i < 1000; i++ ) {
		int res = generateNonUniformDistribution( arr_vec, prob_vec );
		result[res] = result[res] + 1;
	}

	map<int, int>::iterator itRes;
	for ( itRes = result.begin(); itRes != result.end(); itRes++ ) {
		cout << itRes->first << "  " << itRes->second << endl;
	}

	cin.get();
}