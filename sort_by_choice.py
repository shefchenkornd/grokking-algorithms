# dfd

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in xrange(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index



def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		print(i)
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr


a = selectionSort([10,3,8,2,4])
print(a)