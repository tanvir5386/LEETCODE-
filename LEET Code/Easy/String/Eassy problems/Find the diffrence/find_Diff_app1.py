class solution:
    def diff(self,s:str,t:str)->str: #return string here

        mp={}  #blank dictionary create kortse string count er jnno

        for ch in s: #s er sob ch e nebe
            if ch in mp: #
                mp[ch]+=1
            else:
                mp[ch] = 1
        
        for ch in t:
            if ch in mp:
                mp[ch]-=1
            else:
                return ch
            
            if mp[ch]<0:
                return ch

if __name__ == "__main__":
    solution=solution()

    s="abcd"
    t="abcde"

    result=solution.diff(s,t)
    print(f"The extra Character is {result}")