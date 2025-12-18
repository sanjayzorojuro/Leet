class Solution():
    def checkIfPangram(self, sentence):
        return len(set(sentence))>=26

sen=input("Enter a sentence:")   
ob1=Solution()
print(ob1.checkIfPangram(sen))