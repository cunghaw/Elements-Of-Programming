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


int getDistance( LinkedList* start, LinkedList* end ) {
	int res = 0;
	
	while( start != end ) {
		res++;
		start = start->next;
	}
	
	return res;
}

LinkedList* getOverlapList( LinkedList* head1, LinkedList* head2 ) {
	LinkedList* head1_cycle = hasCycle( head1 );
	LinkedList* head2_cycle = hasCycle( head2 );
	
	if ( ( head1_cycle == NULL ) && ( head2_cycle == NULL ) ) {
		return getCommonNode( head1, head2 );
	}
	else if ( ( head1_cycle == NULL ) || ( head2_cycle == NULL ) ) {
		return NULL;
	}
	else {
		LinkedList* temp = head2->next;
		while ( ( temp != head1_cycle ) && ( temp != head2 ) ) {
			temp = temp->next;
		}
		if ( temp == head1_cycle ) {
			int dist1 = getDistance( head1, head1_cycle );
			int dist2 = getDistance( head2, head2_cycle );
			int diff = dist1 - dist2;
			if ( diff > 0 ) {
				while( diff-- > 0 )
					head1 = head1->next;
			}
			else {
				while( diff++ < 0 )
					head2 = head2->next;
			}
			
			while( ( head1 != head2 ) && ( head1 != head1_cycle ) && ( head2 != head2_cycle ) ) {
				head1 = head1->next;
				head2 = head2->next;
			}
			
			if ( head1 == head2 ) {
				return head1;
			}
			else {
				return head1_cycle;
			}
			
		}
		else {
		// disjoint
			return NULL;
		}
	
	}
	
}

int main() {
	
	LinkedList three = { 3, NULL };
	LinkedList two = { 2, &three };
	LinkedList one = { 1, &two };
	LinkedList zero = { 0, &one };
	three.next = &zero;

	LinkedList five = { 5, &one };
	LinkedList four = { 4, &five };

	LinkedList* head = &zero;
	LinkedList* head2 = &four;
	
	LinkedList* res = getOverlapList( head, head2 );
	assert( res->data == 1 | res->data == 0 );
	
	cout << "All unit tests are passed" << endl;

	cin.get();
}