#! /usr/bin/env python
# -*- coding: utf-8 -*-

def quicksort(array):
	if (len(array)) < 2:
		return array
	else:
		# опорный элемент
		pivot = array[0]

		# подмассив всех элементов, меньших опорного
		less = [i for i in array[1:] if i <= pivot]

		# подмассив всех элементов, больших опорного
		greater = [i for i in array[1:] if i > pivot]

		# рекурсия :-)
		return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10, 5, 3, 7]) 