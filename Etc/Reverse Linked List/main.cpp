#include <iostream>

using namespace std;

class LinkedNode
{
public:
	LinkedNode( int num, LinkedNode* node ) : data( num ), next( node )
	{
	};
	
	int data;
	LinkedNode* next;
};

LinkedNode* reverseHelper( LinkedNode* head )
{
	if ( head == NULL )
		return NULL;
		
	LinkedNode* newHead = reverseHelper( head->next );	
	if ( newHead != NULL ) {
		newHead->next = head;
		newHead = head;
		return newHead;
	}
	else
	{
		return head;
	}
};

LinkedNode* reverse( LinkedNode* head )
{
	if ( head == NULL )
		return NULL;
		
	LinkedNode* tail = head;
	while ( tail->next != NULL )
	{
		tail = tail->next;
	}
	LinkedNode* newTail = reverseHelper( head );
	newTail->next = NULL;
	return tail;
};

void printLinkedList( LinkedNode* head )
{
	cout << "LN: ";
	while ( head != NULL )
	{
		cout << head->data << " ";
		head = head->next;
	}
	cout << endl;
};

int main()
{
	LinkedNode* num3 = new LinkedNode( 3, NULL );
	LinkedNode* num2 = new LinkedNode( 2, num3 );
	LinkedNode* head = new LinkedNode( 1, num2 );
	printLinkedList( head );
	head = reverse( head );
	cout << "After reverse " << endl;
	printLinkedList( head );
	cin.get();
};