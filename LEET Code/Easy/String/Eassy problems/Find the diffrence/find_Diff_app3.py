class solve:
    def diff(self, s: str, t: str) -> str:
        xor = 0
        
        # t স্ট্রিংয়ের প্রতিটি অক্ষরের XOR অপারেশন করা
        for ch in t:
            xor ^= ord(ch)
        
        # s স্ট্রিংয়ের প্রতিটি অক্ষরের XOR অপারেশন করা
        for ch in s:
            xor ^= ord(ch)
        
        # XOR এর ফলাফলকে একটি অক্ষরে রূপান্তর করা
        return chr(xor)

if __name__ =="__main__":
    solution=solve()

    s="abcd"
    t="abcde"

    result=solution.diff(s,t)
    print(f"The Extra Charecter is : {result}")
