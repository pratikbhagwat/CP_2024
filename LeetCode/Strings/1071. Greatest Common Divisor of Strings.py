class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        lenGcd = self.getGcdOfLengths(len(str1), len(str2))

        subStrGcd=str1[0:lenGcd]

        constructStr1 = subStrGcd * (len(str1)//lenGcd)
        constructStr2 = subStrGcd * (len(str2)//lenGcd)

        if constructStr1 == str1 and constructStr2 == str2:
            return subStrGcd

        return ""



    def getGcdOfLengths(self,n1,n2):

        for i in range(min(n1,n2), 1,-1):

            if n1%i==0 and n2%i==0:
                return i*self.getGcdOfLengths(n1//i,n2//i)

        return 1



print(Solution().gcdOfStrings("LEET", "ABAB"))