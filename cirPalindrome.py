n = 771 #int(raw_input())
s = 'kjlgjfmenkgllefleenmfiljjiffikeilkmgeneljhekllfhnlfimnmjljlhlljehmniejehfgknnihmhfenihnghgnjkhnfhifglhgenggknnmmjnnnfjmgehlkjkkemiekmlhgggingnjhfgkiejhhfkimenfjkhgfngkniigknlmnifnkiknnjmghmjfneemiikemllgemgmejfkgjinnlfkkjhekmejlleeliinmfeemigkfhlehglegjngelkeeeinhjgkkkllnmmkleekfkfemmeheklffhgimhfmhffnekgkfehkgelielljnkfijghmiimhjelmkgegjehfekfgkjlmekhkfkgfjjkekmjgikjhefgkjmkflhnfflfmjnjelngmgehhmhlgelkljfhhhjnheemfhekemhlkeejmhgljnimgjglfhkkgjkihiinfjmkngmijklhmejljgfglffnfjjjfmlnemhjjllneeihlijljnnlfmiilekeijginjjmjikfmnilmlhmnemijkfnfnjffekfmnnfggfffkfmfjljeknhjgnllhgneilfelekknfimnkhkhkigigjngffffkfeelmilkhjhfhjknfflgfjnkfkifjeifkgjnlgfefghgimfgjkhnnjfijkfgjmflnmihgkjlnljfjeigmjkemfhigekkkgliiemjjfgkhmjhjnniiglelkljmmihiinfkjjnnelfljlehnhehgfkhnmkelhlnjgiii'

strCombinations =[]
maxLen = 0
def checkPalindrome(str):
    mid = (len(str)+2)/2
    for i in xrange(mid):
        if str[i] == str[-(i+1)]:
            continue
        else:
            return False
    return True

def CreateStrCombinations(str):
    for i in xrange(len(str)):
        for j in xrange(i+1,len(str)):
            strCombinations.append(str[i:j+1])

## Check palindrome on initial string
CreateStrCombinations(s)
for comb in strCombinations:
    if (checkPalindrome(comb)):
        maxLen = max(maxLen, len(comb))
    
print (maxLen)
### Check palindrome for transformed string
for i in xrange(1, n):
    s = s[1:] + s[0]
    CreateStrCombinations(s)
    for comb in strCombinations:
        if (checkPalindrome(comb)):
            maxLen = max(maxLen, len(comb))
    print (maxLen)
    maxLen =0
    strCombinations=[]