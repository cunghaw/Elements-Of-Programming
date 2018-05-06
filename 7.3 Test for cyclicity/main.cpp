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

LinkedList* hasCycle( LinkedList* head ) {
	LinkedList* slow = head->next;
	if ( slow == NULL )
		return NULL;

	LinkedList* fast = slow->next;
	while ( ( slow != fast ) && ( slow != NULL ) && ( fast != NULL ) ) {
		slow = slow->next;
		fast = fast->next;
		if ( fast != NULL ) {
			fast = fast->next;
		}
	}
	if ( slow == fast )
	{
		//calculate length of cycle
		LinkedList* temp = fast->next;
		int len = 1;
		while ( temp != fast ) {
			temp = temp->next;
			len++;
		}
		
		temp = head;
		while ( len > 0 ) {
			temp = temp->next;
			len--;
		}
		
		while( temp != head ) {
			temp = temp->next;
			head = head->next;
		}
		return temp;
	}
	else
	{
		return NULL;
	}
};

int main() {

	LinkedList two = { 2, NULL };
	LinkedList five = { 5, &two };
	LinkedList four = { 4, &five };
	LinkedList three = { 3, &four };
	two.next = &three;
	LinkedList one = { 1, &two };
	LinkedList head = { 0, &one };

	LinkedList* res = hasCycle( &head );
	assert( res->data == 2 );
	
	cout << "All unit tests are passed" << endl;

	cin.get();
}