def TowerOfHanoi(n,source,destination,helper):
    if(n==1):
        print("Move Disk from ",source,"to",destination)
        return
    TowerOfHanoi(n-1,source,helper,destination)
    print("Move Disk from ", source, "to", destination)
    TowerOfHanoi(n-1,helper,destination,source)


def main():
    n = int(input())
    TowerOfHanoi(n,1,3,2)

if __name__ =='__main__':
    main()