class solve:
    def diff(self,s:str,t:str)->str:
        sum=0

# t স্ট্রিংয়ের প্রতিটি অক্ষরের ASCII মান যোগ করা
        for ch in t:
            sum+=ord(ch)

        for ch in s:
            sum-=ord(ch)

        return chr(sum)
    
if __name__ =="__main__":
    solution=solve()

    s="abcd"
    t="abcde"

    result=solution.diff(s,t)
    print(f"The Extra Charecter is : {result}")