class Trie:

    def __init__(self):
        self.h={}
        self.st=[]

    def insert(self, word: str) -> None:
        self.h[word]=1
        self.st.append(word)

    def search(self, word: str) -> bool:
        if word in self.h:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for i in range(0,len(self.st)):
          if self.st[i][:len(prefix)]==prefix:
            return True
        return False


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("Re")
param_2 = obj.search("ss")
param_3 = obj.startsWith("Re")
print(param_3)