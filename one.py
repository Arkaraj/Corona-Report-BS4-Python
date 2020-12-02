def all(arr):
    k=len(arr)
    i=0
    while(i<k):
        if(arr[i]==","):
            arr.remove(arr[i])
            k=k-1
            continue
        i=i+1
    return arr




