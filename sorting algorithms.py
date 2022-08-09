# Bubble sort
def bubble_sort(arr_num):
    for i in range(0, len(arr_num)-1):
        print(f"pass ->{i}")
        is_swapped = False
        for j in range(0, len(arr_num)-1):
            if arr_num[j] > arr_num[j+1]:
                arr_num[j+1], arr_num[j] = arr_num[j], arr_num[j+1]
                is_swapped = True
                print(f"arr_content: {arr_num}")
        if not is_swapped:
            print("breaking the main loop due to no more swaps")
            break
    return arr_num

# insertion sort


# Driver code
arr_num = [9,8,7,6,5,4,3,2,1]
arr_num1 = [9,8,7,6,1,2,3,4,5]
#print("final Bubble sort:",bubble_sort(arr_num1))
