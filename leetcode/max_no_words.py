class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        dum=text.split()
        c=0
        d1=0
        print(dum)
        print(brokenLetters)
        for i in range(0,len(dum)):
            for j in brokenLetters:
                if j not in dum[i]:
                    c+=1
            if c==len(brokenLetters):
                d1+=1
            c=0
        return d1
        
        
s=Solution()
print(s.canBeTypedWords( text = "veikxddtjgpixjrux srxiqrczp cxaldqsvsxpzn xrlxovsjy ervh cdtxwnahcvj xazmhniydmzsseuhq htrsuiabtzcjglilehrpxqcadk ynls r pjkiwtcmvldcr t urevy fjmeutye gjnyd wv fueploq eol zofra xnwaxnwh lpckcgzfcslugpmu judahwebqnwtk gfttojiqcffstkcq nfxbw ugnviyeincmuzoosfy kdazdudaztlnj rqg umaohfgtvk i vfhdvuvbih falmmrke rv zsaqn oswdlfq eapt mnr swcoa jhmui t vkm tumfqvj ehcycfgzxjkhxhdbymmwxy xnsxxerahbrr silb rqmhfbyopev fstlsvpblocrvrheghvgiuqftknewskmhbk nchoj bo cxovzradanq fofsrtmnytq brcixelmzvdxmm", brokenLetters = "wqchprenozi"))