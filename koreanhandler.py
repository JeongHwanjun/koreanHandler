class KoreanHandler:
    KOREAN_START=ord("가")
    KOREAN_END=ord("힣")
    KOREAN_HEADS=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    KOREAN_BODIES=['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
    KOREAN_TAILS=[' ','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ',]

    def __init__(self):
        pass

    def isKorean(self,S):
        x=ord(S)
        return x>=self.KOREAN_START and x<=self.KOREAN_END

    def get_korean_head(self,S):
        if not self.isKorean(S[-1]) :
            raise Exception("parameter is not complete korean")
        
        korean=ord(S[-1])
        index=korean-self.KOREAN_START
        return self.KOREAN_HEADS[index//(28*21)]

    def get_korean_body(self,S):
        if not self.isKorean(S[-1]) :
            raise Exception("parameter is not complete korean")
        
        korean=ord(S[-1])
        index=korean-self.KOREAN_START
        return self.KOREAN_BODIES[(index//28)%21]

    def get_korean_tail(self, S):
        if not self.isKorean(S[-1]) :
            raise Exception("parameter is not complete korean")
        
        korean=ord(S[-1])
        index=korean-self.KOREAN_START
        return self.KOREAN_TAILS[index%28]
    
    def split_korean(self,S,seperator='/'):
        result=[]
        for korean in S:
            if not self.isKorean(korean):
                raise Exception("parameter is not complete korean")
            
            result.append(self.get_korean_head(korean))
            result.append(self.get_korean_body(korean))
            result.append(self.get_korean_tail(korean))
            
            result.append(seperator)
        
        return result
    
    def join_korean(self,S,seperator='/'):
        result=''
        i=0
        while i<len(S):
            korean=0
            Head=S[i]
            if Head not in self.KOREAN_HEADS:
                raise Exception("wrong sequence of korean")
            Body=S[i+1]
            if Body not in self.KOREAN_BODIES:
                raise Exception("wrong sequence of korean")
            korean+=self.KOREAN_HEADS.index(Head)*28*21
            korean+=self.KOREAN_BODIES.index(Body)*28
            #일단 초성과 중성은 있는게 확실하므로 조합해놓는다.
            
            #그러나 종성은 없을 수도 있고, 입력시 공백/빈 문자열로 들어오거나 아예 생략되어 들어오는 경우가 있으므로 처리해준다.
            Tail=S[i+2]
            if Tail == seperator or Tail == '' :
                result += chr(korean+self.KOREAN_START)
                if Tail == seperator: i+=3
                else: i+=4
                continue
            elif Tail not in self.KOREAN_TAILS:
                raise Exception("wrong sequence of korean")
            
            korean+=self.KOREAN_TAILS.index(Tail)
            
            result += chr(korean+self.KOREAN_START)
            i+=4
        return result