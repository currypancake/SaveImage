# 설명서
**하나도 안 복잡하니까 포기하지말고 끝까지 따라해보셈**
중간에 이해못하겠거나 실행 안되면 나 호출 ㄱㄱ

결과물↓
![res1]('https://github.com/currypancake/SaveImage/blob/master/image/res1.png')
![res2]('https://github.com/currypancake/SaveImage/blob/master/image/res2.png')
![res3]('https://github.com/currypancake/SaveImage/blob/master/image/res3.png')


## 필수 설치
* 파이썬

* 라이브러리
파워쉘을 열고 (파워쉘을 여는 법 - https://www.manualfactory.net/11724)
pip install requests
pip install BeautifulSoup
위 두줄을 복붙하고 엔터를 누릅니다.

설치가 안돼있으면 안돌아갑니다.

## 보안코드와 쿠키
카드 보안코드 뜯는 법은 알거라 생각하고 뜯는 방법에 대해서는 다루지 않겠음
save_image.py 파일을 열면 6번째 줄에 scode = '' 라고 써 있는데 따옴표 사이에 보안코드 넣으면 됨 (언더바 포함)
ex) 세무조커 난쟈타운 콜라보 이벤트 같은 경우는 scode = '_59822b672f' 이럼

8번째 줄을 보면 login_cookie='' 일케 되있는데 이거 채우는 법은

1. 컴터로 꼬추에 접속한다.
2. 로그인이 안되어있으면 로그인을 한다.
3. 모바게 페이지로 이동한다. https://sp.mbga.jp/?_from=globalfooter
4. 개발자 툴에서 Application 탭으로 이동한다.
5. 그리고 이미지처럼 SP_LOGIN_SESSION 이라고 써있는걸 누르고 아래 내가 빨간색으로 가려둔 걸 복붙해서 따옴표 안에 넣으면 됨
![개발자 툴 Application 탭]('https://github.com/currypancake/SaveImage/blob/master/image/cookie.png')
이거 그냥 개인정보라고 생각하면 편함 그러니까 남들한테 보여주지 마셈


## 실행법
1. save_image.py 파일이 있는 폴더에서 파워쉘을 연다. (파워쉘을 여는 법 - https://www.manualfactory.net/11724)
2. python3 save_image.py <= 이거 복붙하고 엔터


## 주의사항
이거 원리가 그냥 꼬추 이미지 주소 하나하나 들어가서 있는지 체크하고 있으면 다운로드하는거라 **존나 느림**
그리고 카드 숫자 범위도 그냥 임의로 정해준거라 나중에 님들이 범위 수정해야함

save_image.py 파일을 보면
~~~py
def findSRImage(): # <= 스알 
	# 쥬피터 ~ 코가도
	for i in range(1, 41) :
		for j in range(25, 40) : #SR번호 25~39(40 미포함)까지 이미지 있는지 확인
			checkCard(i, j)

	# 깃발 ~ 레제
	for i in range(42, 47) :
		for j in range(17, 40) : #SR번호 25~39(40 미포함)까지 이미지 있는지 확인
			checkCard(i, j)

def findRImage(): # <= 레어
	# 쥬피터 ~ 레제
	for i in range(1, 47) :
		for j in range(17, 40) : #R번호 17~39(40 미포함)까지 이미지 있는지 확인
			find = isImage('R', i, j, 'P')
			if find == True:
				saveAllImage('R', i, j)

~~~
이렇게 되어 있는데 

~~~py
for j in range(25, 40)
~~~
이 부분이 앨범 검사 범위임. 25번에서 39번까지만 검사함.(40전까지만 검사)

그러니까
01jupiter_01toumaa_2_SR25.png 에서 01jupiter_01toumaa_2_SR39.png 까지만 체크하는 거임

만약 숫자를 
~~~py
for j in range(10, 15)
~~~
이렇게 바꿨으면
01jupiter_01toumaa_2_SR10.png 에서 01jupiter_01toumaa_2_SR14.png 까지만 체크하는 거임

그래서 나중에 카드 수 존나 많아져서 스알번호 마지막이 40이면 님들이 
~~~py
for j in range(40, 50)
~~~
이런식으로 수정해야한다는 뜻임 ㅇㅋ??

그리고 카드 이름 일단 내가 쓰던 형식으로 해놨는데 불만 있어도 참으셈 ㅎㅎ
근데 문제가 카드 번호같은게 내가 알기론 일단 츠바사가 번호가 한칸씩 밀린거로 알아서 나중에 이름 직접 수정해야함
내가 이거 하나하나 처리는 못해서 그냥 나중에 위키에 이미지 올릴때 중복파일이다 어쩌고 하면 그때 직접 고치셈 ㅎㅎ
