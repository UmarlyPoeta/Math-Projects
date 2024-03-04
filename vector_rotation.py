

def rotate_vector(vector,n):
    k=0
    j=n-1
    while j>=k:
        tmp=vector[k]
        vector[k]=vector[j]
        vector[j]=tmp
        k=k+1
        j=j-1
    return vector



def main():
    n=int(input("Give the dimension of vector: "))
    vector=[]
    for i in range(1,n+1):
        vector.append(int(input(f"Give {i} parameter of a vector: ")))
    print(f"Your vector is {vector}")
    print(f"rotation of that vector looks like {rotate_vector(vector,n)}")

if __name__=="__main__":
    main()
    exit()