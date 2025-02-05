def twoSum(nums,target):
    num_map={} 

    for i ,num in enumerate(nums):
        remainig=target-num  

        if remainig in num_map:
            return[num_map[remainig],i]

        num_map[num]=i  
    return []
  
if __name__ == "__main__":
    nums=list(map(int,input("Enter numbers comma separated: ").split(",")))
    target=int (input("Enter Target sum: "))

    result= twoSum(nums,target)

    print("Output:",result)


