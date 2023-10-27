# 20223075 목진협
## 유레카프로젝트 Git Blog 만들기 

## Welcome To Mok's World!
[Mok's World!](https://jinhyup-mok.github.io/)

## Build Process
### 1. Repository 생성 및 Local-Remote Repository 연동
- Github에서 <username>.github.io 이름의 Repository 생성한다.

### 2. Local-Remote Repository 연동
1. Remote Repository의 주소를 복사  
2. `git clone <복사한 Remote repository의 주소> <path>`로 clone  
3. `git commit -m "<commit msg>"`로 커밋, 메시지 남기기  
4. `git branch -M main`으로 현재 branch의 이름을 main으로 변경한다.  
5. `git status`로 현재 상태 확인 후 `git add .`로 변경파일을 추가한다.  
6. `git push origin main`으로 main에 로컬 변경사항 push (토큰 필요)

### 3. Jekyll 사용하기

- [jekyll 설치 가이드](https://jekyllrb-ko.github.io/docs/installation/ubuntu/)
  - 위 링크를 이용해서 Jekyll을 설치하기 전, 필요한 모든 의존요소를 가지고 있는지 확인하고 일반 사용자 계정에 젬 설치 디렉토리를 설정
- Jekyll과 Bundler 설치
  - `gem install jekyll bundler`
- Jekyll이 올바르게 설치되었는지 확인
  - `jekyll -v`

### 4. Jekyll 사이트 생성하기

- 현재 디렉토리(.)(=clone한 디렉토리)에 Jekyll을 설치
  - `jekyll new . --force`
- Jekyll 시작하기
  - `bundle exec jekyll serve`
  - localhost:4000 접속

### 5. Themes 적용
[Jekyll Themes](http://jekyllthemes.org/)에서 사용하고 싶은 Jekyll 테마를 선택한다.  
1. 선택한 테마의 Git 레포지토리를 Fork 한다  
2. Fork한 레포지토리를, `<username>.github.io` 이름의 Repository를 생성하여 테마를 적용한다.  

### 6. 파비콘(Favicon) 추가
내가 사용한 Jeykll 테마 (lanyon)에는 Favicon 설정 코드가 내장 되어있기 때문에, 이미지 파일만 추가해주면 된다.  
  - **public** 폴더의 **favicon.ico** 파일과 해당 폴더 아래에 자신이 원하는 이미지를 추가한다.

### 7. User Setting
> 모든 문서 편집은 Markdown으로 작성한다.

**_config.yml** 파일에서 블로그 이름, 프로필, 블로그 기본 정보  

```
title: Mok's World !
email: mokjh1117@kookmin.ac.kr
description: >- # this means to ignore newlines until "baseurl:"
  " Aim 1st "
baseurl: "" # the subpath of your site, e.g. /blog
url: "" # the base hostname & protocol for your site, e.g. http://example.com
twitter_username: jekyllrb
github_username:  Jinhyup-Mok
```
**_posts** 폴더에서 블로그 포스팅을 진행한다.
  - _posts에 **YYYY-MM-DD-TITLE.md** 형식으로 새로운 포스트 문서를 작성한다.
  ```
  ---
  layout: post
  title: "제목"
  comments: true
  last_modified_at: 2022-11-26T13:56:10-58:00
  ---
  
  ## <포스트 제목>
  [......포스트 내용 작성......]
  
  ```
  
**Google Analytics에 대한 내용은 블로그에 포스팅 되어있다.**

### 8. Disqus 추가하기

  1. [Disqus](https://disqus.com/) 가입하기  
  2. "I want to install Disqus on my site" 클릭  
  3. 사이트 정보 입력  
  4. Platform 중 **Jekyll** 선택  
  5. Install Instruction을 읽어본 후 **Configure**를 눌러 다음을 진행  
  6. **Website URL**에 자신 블로그 주소 입력 후 Next  
  7. Comment 정책 선택 및 동의  
  8. Complete Setup 클릭  
  9. **_config.yml**에 아래의 Key, Value 추가  
  ```
  comment:
  provider: "disqus"
  disqus:
    shortname: "Jade"
    
  ```
  10. **_layout** 폴더의 **post.html**파일에 Universal Code를 추가  
  ```
  <h2>Comments</h2>
  <div id="disqus_thread"></div>
  <script>
      /**
      *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
      *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
      let PAGE_URL = "{{site.url}}{{page.url}}"
      let PAGE_IDENTIFIER = "{{page.url}}"
      var disqus_config = function () {
      this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
      this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
      };

      (function() { // DON'T EDIT BELOW THIS LINE
      var d = document, s = d.createElement('script');
      s.src = 'https://jinhyup-mok-github-io.disqus.com/embed.js';
      s.setAttribute('data-timestamp', +new Date());
      (d.head || d.body).appendChild(s);
      })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by   Disqus.</a></noscript>
  ```
11. 블로그 post파일 아래에 `comments: true` 코드 추가

### 감사합니다. *fin*
