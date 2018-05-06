#include <iostream>
#include <locale>
#include <string>
#include <cassert>

using namespace std;

bool isPalindromeHelper( const string& str, int start, int end ) {
	while ( isalpha( str[start] ) == 0 && ( start < end ) )
		start++;
		
	while ( isalpha( str[end] ) == 0 && ( start < end ) )
		end--;
		
	if ( start == end ) {
		return true;
	}
	else if ( start < end ) {	
		if ( toupper( str[start] ) == toupper( str[end] ) )
			return isPalindromeHelper( str, start + 1, end - 1 );
		else
			return false;
	}
	else {
		return false;
	}
}

bool isPalindrome( const string& str ) {
	return isPalindromeHelper( str, 0, str.size() - 1 );
}

int main() {
	string str1( "A man, a plan, a canal, Panama" );
	string str2( "Able was I, ere I saw Elba!" );
	string str3( "Ray a Ray" );

	assert( isPalindrome( str1 ) == true );
	assert( isPalindrome( str2 ) == true );
	assert( isPalindrome( str3 ) == false );
	
	cout << "All unit tests are passed" << endl;

	cin.get();
}