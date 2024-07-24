# koreanHandler

---

한글을 다루는 클래스입니다. 

---

### 사용 방법  
koreanhandler.py를 다운받아 

    from koreanhandler import KoreanHandler
    KH=KoreanHandler()


#### KoreanHandler.isKorean(S)  
S가 완전한 한글인지 확인합니다.  
완전한 한글(예 : '가')이라면 True, 완전하지 않은 한글(예 : 'ㄱ', 'ㅏ')이라면 False를 반환합니다.

    KH.isKorean('각') # True
    KH.isKorean('KH') # False
    KH.isKorean('ㄱ') # False

#### KoreanHandler.get_korean_head(S)
S의 초성을 반환합니다.  
만약 S가 완전한 한글이 아니라면, 예외를 발생시킵니다.

    KH.get_korean_head('갈') # 'ㄱ'
    KH.get_korean_head('ㅋ') # throw Exception
    KH.get_korean_head('KH') # throw Exception

#### KoreanHandler.get_korean_body(S)  
S의 중성을 반환합니다.  
나머지 동작은 `KoreanHandler.get_korean_head(S)`와 동일합니다.

    KH.get_korean_body('갈') # 'ㅏ'

#### KoreanHandler.get_korean_tail(S)  
S의 종성을 반환합니다. 종성이 없다면 `' '`를 반환합니다.  
나머지 동작은 `KoreanHandler.get_korean_head(S)`와 동일합니다.

    KH.get_korean_tail('갈') # 'ㄹ'
    KH.get_korean_tail('가') # ' '

#### KoreanHandler.split_korean(S, seperator='/')
S를 초성, 중성, 종성으로 나눈 배열을 반환합니다.  
글자간의 구별은 기본적으로 `'/'`를 사용합니다.  
종성이 없는 한글의 경우,  `' '`로 표시합니다. S가 완전한 한글로 이루어진 문자열이 아니라면, 예외를 발생시킵니다.

    KH.split_korean('화염구') # ['ㅎ', 'ㅘ', ' ', '/', 'ㅇ', 'ㅕ', 'ㅁ', '/', 'ㄱ', 'ㅜ', ' ', '/']
    KH.split_korean('화염구','!') # ['ㅎ', 'ㅘ', ' ', '!', 'ㅇ', 'ㅕ', 'ㅁ', '!', 'ㄱ', 'ㅜ', ' ', '!']
    KH.split_korean('ㅁㅢ') # throw Exception

#### KoreanHandler.join_korean(S, seperator='/')
S를 온전한 한글 문자열로 만들어 반환합니다.  
이때, S는 `KoreanHandler.split_korean(S, seperator='/')`에서 반환하는 것과 같은 형식으로 주어져야 합니다.  
`seperator`가 올바르다면, 종성은 생략해도 상관 없습니다.  
한글이 올바른 순서로 주어지지 않거나(예 : `['ㄱ', 'ㅏ', 'ㅏ']`), `seperator`를 생략하면 예외를 발생시킵니다.

    KH.join_korean(['ㅎ', 'ㅘ', ' ', '/', 'ㅇ', 'ㅕ', 'ㅁ', '/', 'ㄱ', 'ㅜ', ' ', '/']) # '화염구'
    KH.join_korean(['ㅎ', 'ㅘ', '/', 'ㅇ', 'ㅕ', 'ㅁ', '/', 'ㄱ', 'ㅜ', '/']) # '화염구'
    KH.join_korean(['ㅎ', 'ㅘ', '/', 'ㅇ', 'ㅕ', 'ㅁ', '/', 'ㅄ', 'ㅜ', '/']) # throw Exception ('ㅄ'은 올바른 초성이 아님)

---

추후에 더 많은 기능을 추가하고, 기존의 기능을 개선하고, 더욱 사용하기 쉽게 바꿀 예정입니다.
