#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

template< class T >
class CircularQueue {
	
public:
	explicit CircularQueue( int size ) : mData( size ), mSize( 0 ), mCapacity( size ), mHeadIdx( 0 ), mTailIdx( -1 ) 
	{
	};
	
	virtual ~CircularQueue()
	{
	};

	void enqueue( int data )
	{
		if ( mSize + 1 > mCapacity )
			resizeAndCopy();
	
		mTailIdx = incIdx( mTailIdx );
		mData[ mTailIdx ] = data;
		mSize++;
	};

	int dequeue()
	{
		if ( mSize == 0 )
			throw "No data to dequeue";

		int res = mData[ mHeadIdx ];
		mHeadIdx = incIdx( mHeadIdx );
		mSize--;
		return res;
	};

	int size()
	{
		return mSize;
	}

private:

	int incIdx( int data )
	{
		data++;
		data = data % mCapacity;
		return data;
	};

	void resizeAndCopy()
	{
		vector<int> temp;
		mCapacity = 2 * mCapacity;
		temp.resize( mCapacity );
		int startIdx = mHeadIdx;
		int endIdx = mTailIdx;
		int idx = 0;
		while ( startIdx != endIdx )
		{
			temp[idx++] = mData[startIdx];
			startIdx = incIdx( startIdx );
		}
		temp[idx] = mData[startIdx];
		mHeadIdx = 0;
		mTailIdx = idx;
		mData = temp;
	}

	vector<T> mData;
	int mSize;
	int mCapacity;
	int mHeadIdx;
	int mTailIdx;
};


int main() {
	CircularQueue<int> queue( 3 );
	
	queue.enqueue( 1 );
	queue.enqueue( 2 );
	queue.enqueue( 3 );
	assert( queue.size() == 3 );
	assert( queue.dequeue() == 1 );
	assert( queue.dequeue() == 2 );
	assert( queue.size() == 1 );
	assert( queue.dequeue() == 3 );

	queue.enqueue( 1 );
	queue.enqueue( 2 );
	queue.enqueue( 3 );
	queue.enqueue( 4 );
	queue.enqueue( 5 );
	queue.enqueue( 6 );
	assert( queue.size() == 6 );
	assert( queue.dequeue() == 1 );
	assert( queue.dequeue() == 2 );
	assert( queue.dequeue() == 3 );
	cout << "All unit tests are passed" << endl;
	cin.get();
	return 0;
}