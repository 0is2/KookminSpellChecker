# 국민 맞춤법 검사기

## 사용 방법

### 1. 카카오i 오픈빌더 시작하기

1. 카카오i 오픈빌더 접속

   - https://i.kakao.com/openbuilder/

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/1.png">

2. 새로운 봇 생성

      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/2.PNG">

3. kakao for business 접속

   - https://i.kakao.com/openbuilder/

      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/3.PNG">

### 2. 카카오톡 채널 연결

1. 카카오톡 채널 생성

      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/4.PNG">

2. 카카오톡 채널 연결

      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/5.PNG">

### 3. 구름IDE로 웹서버 구현

1. 다운로드

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/100.png">

2. 구름IDE 접속 (http:// ide.goorm.io)

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/101.png">

3. 컨테이너 생성

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/102.png">

4. 다운로드 받은 파일 가져오기

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/103.png">

5. Flask 설치

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/104.png">

6. 실행 URL과 포트 설정

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/105.png">

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/106.png">

7. 웹서버 실행

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/107.png">

### 4. 기능 구현

1. 각 기능 별 스킬 작성

      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/6.png">

2. 웹 서버 URL 입력
  - 구름IDE에서 컨테이너 - 포트포워딩 설정을 통해 URL 작성
      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/7.png">

3. 각 기능 별 블록 작성

      <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/8.png">

4. 스킬과 블록 연결

   - 파라미터 설정 - 스킬 선택

     봇 응답 - 스킬데이터 사용 선택

     <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/9.PNG">

### 5. 시나리오 작성

1. 웰컴 블록 작성

     <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/10.PNG">

2. 폴백 블록 작성

   <img src="https://github.com/0is2/KookminSpellChecker/blob/master/pic/11.PNG">

## 라이브러리에 대한 안내

이 라이브러리는 네이버 한글 맞춤법 검사기를 바탕으로 만들어진 라이브러리인 py-hanspell을 사용하였습니다.

py-hanspell에 대한 자세한 사용 방법은 [링크](https://github.com/ssut/py-hanspell)를 참고하십시오.

