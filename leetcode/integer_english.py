class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=1
        dummy=""
        self.func(num,n,dummy)
    
    def func(self,num,n,dummy):
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        num1=num%10
        num=num-num1
        num=num//10
        print(num1," ",num)
        if num*10==100 or num*10==1000 or num*10==1000000 or num*10==1000000000:
            dummy=d[num*10]
            num=0
        elif n==1 or n==100 or n==1000 or n==100000 or n==1000000:
            
            if n==100 or n==1000 or n==1000000 :
                dummy=d[num1]+" "+d[n]+" "+dummy
            elif n==100000:
                dummy=d[num1]+" "+d[100]+" "+dummy
            else:
                dummy=d[num1]+" "+dummy
        else:
              dummy=d[num1*10]+" "+dummy
        n=n*10
        if num==0:
            dummy=dummy.replace("Ten One",d[11])
            dummy=dummy.replace("Ten Two",d[12])
            dummy=dummy.replace("Ten Three",d[13])
            dummy=dummy.replace("Ten Four",d[14])
            dummy=dummy.replace("Ten Five",d[15])
            dummy=dummy.replace("Ten Six",d[16])
            dummy=dummy.replace("Ten Seven",d[17])
            dummy=dummy.replace("Ten Eight",d[18])
            dummy=dummy.replace("Ten Nine",d[19])
            dummy=dummy.replace("Ten Zero",d[10])
            dummy=dummy.replace("Two Zero",d[20])
            dummy=dummy.replace("Three Zero",d[30])
            dummy=dummy.replace("Four Zero",d[40])
            dummy=dummy.replace("Five Zero",d[50])
            dummy=dummy.replace("Six Zero",d[60])
            dummy=dummy.replace("Seven Zero",d[70])
            dummy=dummy.replace("Eight Zero",d[80])
            dummy=dummy.replace("Nine Zero",d[90])
            dummy=dummy.replace("Twenty Zero","Twenty")
            dummy=dummy.replace("Thirty Zero","Thirty")
            dummy=dummy.replace("Forty Zero","Forty")
            dummy=dummy.replace("Fifty Zero","Fifty")
            dummy=dummy.replace("Sixty Zero","Sixty")
            dummy=dummy.replace("Seventy Zero","Seventy")
            dummy=dummy.replace("Eighty Zero","Eighty")
            dummy=dummy.replace("Ninety Zero","Ninety")
            
            print(dummy)
            return 0
        self.func(num,n,dummy)
        
s=Solution()
s.numberToWords(num = 1505)