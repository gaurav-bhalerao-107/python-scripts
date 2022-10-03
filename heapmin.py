###This is a program for creating a min-heap
def heapify(arr,n,i):
    smallest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify(arr,n,smallest)
def buildheap(arr,n):
    startInd=n//2 -1
    for i in range(startInd,-1,-1):
        heapify(arr,n,i)
def printheap(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()    
if __name__=="__main__":
    arr=[3,1, 5, 4, 6, 13,10, 9, 8, 15, 17];
    n=len(arr)
    buildheap(arr,n)
    printheap(arr,n)
