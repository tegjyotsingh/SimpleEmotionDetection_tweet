#Author: Tegjyot Singh Sethi
#Module for Performing the Quick Sort.


#Function for exchanging two values of a list
def exchange(List,i,j):
	temp=List[i]
	List[i]=List[j]
	List[j]=temp

#QuickSort1 is the function API to call the Quicksort which takes the last element as the Pivot
def quicksort1(List):

	quicksort1_orig(List,0,len(List)-1)
	return List

def quicksort1_orig(A,p,r):
	if p<r:
		q=partition1(A,p,r)
		quicksort1_orig(A,p,q-1)
		quicksort1_orig(A,q+1,r)
	

def partition1(A,p,r):
	x=A[r]
	i=p-1
	for j in range(p,r):
		if A[j]<=x:
			i+=1
			exchange(A,i,j)
	exchange(A,i+1,r)
	return i+1

#Quick Sort is the Function API which takes the first element of the list as a pivot
def quicksort2(List):
	quicksort2_orig(List,0,len(List)-1)
	return List

def quicksort2_orig(A,p,r):
	if p<r:
		q=partition2(A,p,r)
		quicksort2_orig(A,p,q-1)
		quicksort2_orig(A,q+1,r)
	

def partition2(A,p,r):
	
	x=A[p]
	i=p
	for j in range(p+1,r+1):
		if A[j]<=x:
			i+=1
			exchange(A,i,j)
	exchange(A,p,i)
	return i

#Function for testing the given quicksort routines
def main():
	X=[1,2,3,6,4,4,7,9,5]
	quicksort1(X)
	print X
	X=[5,4,6,3,1,8,7]
	quicksort2(X)
	print X

if __name__=='__main__':
	main()
			
