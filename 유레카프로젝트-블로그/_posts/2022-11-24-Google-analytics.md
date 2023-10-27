---
layout: post
title: About Google Analytics
comments: true
---
Google Analytics는 현재 구글 마케팅 플랫폼 브랜드 내의 플래솜으로서, 웹사이트 트래픽을 추적하고 보가하는 구글이 제공하는 웹 애널리틱스 서비스이다.

------------
## 시작하기

1. Google Analytics에 들어가서 계정 생성
2. 데이터 스트림 웹 항목에 본인 블로그 주소를 입력하여 스트림 추가 (측정항목 선택은 자유롭게)
3. 블로그에 사용할 측정 ID확인  
    - 측정 ID 형식
        - Google 애널리틱스 4 형식 : G-XXXXXXXX
        - 유니버설 애널리틱스 형식 : UA-XXXXXXXX-X

--------------
## 블로그에 추가하기
나의 블로그의 `__config.yml` 이 `Google Analytics id, e.g. G-XXXXXXXX`이기 때문에, **Google 애널리틱스 4**를 기준으로 설정해야 한다.  
```
google_analytics:
  provider: "google"
  google:
    # traking_id : UA-250341310-1
    traking_id : G-ZMB3QRZWGX
```
- 스크립트는 생성한 계정 좌측 상단바 가장 하단에 위치한 톱니바퀴모양 설정 > 속성탭 데이터 스트림 > 계정생성할때 생성했던 스크림을 선택한다.
- 새로운 온페이지 태그 추가 탭의 직접 설치 항목을 클릭하여 소스코드를 복사한다.
```
<!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=[본인의 ID]"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', '본인의 ID');
  </script>
```
- 블로그 폴더의 `_includes`로 이동하여 `<head>`에 해당하는 코드가 적혀있는 파일에 위 코드를 삽입한다.  
- Github에 수정한 소스코드를 올리고, 개발자 도구를 켜고 `gtag` 를 입력해본다.
    - `ƒ gtag(){dataLayer.push(arguments);}`이라는 메시지가 뜨면 성공!  

설정을 마친 후 Google analytics 사이트로 이동하여, 데이터 수집이 활성화 되어있는지 확인한다.