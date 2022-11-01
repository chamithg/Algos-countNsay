class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = 1
        strn= "1"
        for i in range(n-1):
            strn = self.num_to_say(num)
            num = self.say_to_num(strn)
        
        return strn

    def num_to_say(self,num):
        output = ""
        tempCount =0
        for i in range(len(str(num))):
            if i ==0 or str(num)[i] == str(num)[i-1]:
                tempCount +=1
            else:
                output += str(tempCount)
                output += str(num)[i-1]
                tempCount =1
                
            if i == len(str(num))-1:
                output += str(tempCount)
                output += str(num)[i]
        return output
    
    def say_to_num(self,strn):
        return int(strn)
            
            


count = Solution()

n = 1
print(count.countAndSay(4))
            

