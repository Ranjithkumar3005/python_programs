class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods=foods
        self.cuisines=cuisines
        self.ratings=ratings

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        print(self.ratings)
        for i in range(0,len(self.foods)):
            if food==self.foods[i]:
                self.ratings[i]=newRating
        print(self.ratings)
        
    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        dummy=0
        summy=[]
        for i in range(0,len(self.cuisines)):
            if cuisine==self.cuisines[i]:
               if dummy==self.ratings[i]: 
                   dummy=self.ratings[i]
                   summy.append(self.foods[i])
               elif dummy<self.ratings[i]:
                   dummy=self.ratings[i]
                   summy=[]
                   summy.append(self.foods[i])
        summy.sort()
        
        return str(summy[0])


# Your FoodRatings object will be instantiated and called as such:
obj = FoodRatings(["kimchi","miso","rahi","moussaka","raten","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,9,16,15,1,7])
obj.changeRating("raten",16)
param_2 = obj.highestRated("japanese")
print(param_2)