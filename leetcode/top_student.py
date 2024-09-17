class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        pos={}
        neg={}
        for i in positive_feedback:
            pos[i]=1
        for i in negative_feedback:
            neg[i]=1
        h={}
        for i in range(0,len(report)):
            c=0
            val=report[i].split(" ")
            for j in val:
                if j in pos:
                    c+=1
                elif j in neg:
                    c-=1
            h[student_id[i]]=c
        sorted_d = sorted(h.items(), key=lambda x: (-x[1], x[0]))
        dum=[]
        for i in range(0,k):
            dum.append(sorted_d[i][0])
        print(dum)
        
        


s=Solution()
s.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious smart","the student is smart"], student_id = [1,2], k = 2)