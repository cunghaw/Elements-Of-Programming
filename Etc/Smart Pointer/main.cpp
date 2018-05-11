#include <iostream>
#include <cassert>

using namespace std;

template< class T >
class SmartPointer 
{
public:

	explicit SmartPointer( T* ptr );
	~SmartPointer();
	
	T& operator*();
	T* operator->();

	SmartPointer( const SmartPointer& smptr );
	SmartPointer& operator= ( const SmartPointer& smptr);
	
private:

	T* mPtr;
	int* mCount;
};

template< class T >
SmartPointer<T>::SmartPointer( T* ptr ) : mPtr( ptr ), mCount( NULL )
{
	mCount = new int( 1 );
};

template< class T >
SmartPointer<T>::~SmartPointer()
{
	*mCount = *mCount - 1;
	if ( *mCount == 0 )
	{
		delete mCount;
		delete mPtr;
		mPtr = NULL;
		mCount = NULL;
		cout << "successfully delete pointer from destructor" << endl;
	}
};

template< class T >
T& SmartPointer<T>::operator*()
{
	return *mPtr;
};

template< class T >
T* SmartPointer<T>::operator->()
{
	return mPtr;
};

template< class T >
SmartPointer<T>::SmartPointer( const SmartPointer& smptr )
{
	mPtr = smptr.mPtr;
	mCount = smptr.mCount;
	*mCount = *mCount + 1;
};

template< class T >
SmartPointer<T>& SmartPointer<T>::operator= ( const SmartPointer& smptr)
{
	if ( this != &smptr )
	{
		*mCount = *mCount - 1;
		if ( *mCount == 0 )
		{
			delete mCount;
			delete mPtr;
			mPtr = NULL;
			mCount = NULL;
			cout << "successfully delete pointer from copy assignment" << endl;
		}		
	
		mPtr = smptr.mPtr;
		mCount = smptr.mCount;
		*mCount = *mCount + 1;
	}
	return *this;
};

int main()
{
	if ( true )
	{
		int* ctr = new int( 2 );
		int* ptr = new int( 1 );
		SmartPointer<int> testPtr( ptr );
		SmartPointer<int> testPtr2( testPtr );
		SmartPointer<int> testPtr3( ctr );
		testPtr3 = testPtr;
		assert( *testPtr == 1 );
		assert( testPtr.operator->() == ptr );
	}
	cin.get();
}