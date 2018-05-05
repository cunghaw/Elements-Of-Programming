#include <iostream>
#include <cassert>
#include <map>

using namespace std;

double computeHelper( double x, int y, map<int, double>& cache ) {
	if ( y == 0 ) {
		return 1;
	}
	else if ( y == 1 ) {
		return x;
	}
	else {
		map<int, double>::iterator it = cache.find( y );
		if ( it == cache.end() ) {
			double result = computeHelper( x, y / 2, cache ) * computeHelper( x, y - y / 2, cache );
			cache[ y ] = result;
			return result;
		}
		else
			return it->second;
	}
}

double compute( double x, int y, map<int, double>& cache ) {
	if ( y < 0 ) {
		x = 1/x;
		y = -1 * y;
	}
	return computeHelper( x, y, cache );
}

int main()
{
	map<int, double> cache;
	assert( compute( 3.0, 3, cache ) == 27.0 );
	cache.clear();
	assert( compute( 2.0, -2, cache ) == 0.25 );
	cout << "All unit tests are passed" << endl;
	cin.get();
	return 1;
}