#include <iostream>
#include <locale>
#include <string>
#include <cassert>

using namespace std;

struct LinkedList 
{
	int data;
	LinkedList* next;
};

int getLength( LinkedList* head ) {
	int res = 0;
	
	while ( head != NULL ) {
		res++;
		head = head->next;
	}
	
	return res;
};

LinkedList* getCommonNode( LinkedList* head, LinkedList* head2 ) {
	int len_head = getLength( head );
	int len_head2 = getLength( head2 );
	int diff = len_head - len_head2;
	if ( diff > 0 ) {
		while ( diff-- > 0 )
			head = head->next;
	}
	else {
		while ( diff++ < 0 )
			head2 = head2->next;
	}
	
	while ( ( head != head2 ) && ( head != NULL ) && ( head2 != NULL ) ) {
		head = head->next;
		head2 = head2->next;
	}
	
	if ( head == head2 )
		return head;
	else 
		return NULL;
};

int main() {
	
	LinkedList three = { 3, NULL };
	LinkedList two = { 2, &three };
	LinkedList one = { 1, &two };
	LinkedList zero = { 0, &one };

	LinkedList five = { 5, &one };
	LinkedList four = { 4, &five };

	LinkedList* head = &zero;
	LinkedList* head2 = &four;
	
	LinkedList* res = getCommonNode( head, head2 );
	assert( res->data == 1 );
	
	cout << "All unit tests are passed" << endl;

	cin.get();
}