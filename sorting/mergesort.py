
numbers = [3, 99, 0, 7, 5]

def merge(start, mid, end):
    newArr = []

    

def merge_sort(start, end):

    if start < end:
        mid = (start + end)//2

        merge_sort(start, mid)
        merge_sort(mid+1, end)

        merge(start, mid, end)

merge_sort(0, len(numbers)-1)
