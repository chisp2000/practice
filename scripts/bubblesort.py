


def bubblesort(elements):
  # Looping from size of array from last index[-1] to index [0]
  for n in range(len(elements)-1, 0, -1):
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # swapping data if the element is less than next element in the array
        elements[i], elements[i + 1] = elements[i + 1], elements[i]



lst = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)



bubblesort(lst)

print(lst)
