---
layout: post
title: What's Jekyll?
comments: true
---

## Jekyll
설치형 블로그의 하나, Ruby를 기반으로 만들어져 있다.
 > Jekyll is a simple, blog aware, static site generator. It takes a template directory [...] and spits out a complete, static website suitable for serving with Apache or your favorite web server. This is also the engine behind GitHub Pages, which you can use to host your project’s page or blog right here from GitHub.

-------------
## Jekyll 특징
마크다운을 사용해서 포스트를 작성하면 HTML으로 변환하여 정적 사이트를 만들어준다. 마크다운의 특성상 코드 표현이나 이미지 삽입, 링크, 테이블 표현이 간단하고, GitHub Pages등에서 무료 호스팅을 제공하기 때문에 개발자들 사이에서는 인지도가 어느 정도 있는 편이다. 검색 엔진에서 필요로 하는 sitemap.xml과 robots.txt 또한 자동적으로 생성된다. 물론, 구글 검색 엔진 등에 검색되기 위해서는 이것 이외에도 헤드 태그에 google-site-verification을 추가해야 한다.

변수 같은 경우 YAML 프론트메터를 사용하기에 사이트 제목/저작자 등을 변수로 지정하여 동적인 사용을 돕는다. 스타일 또한 동적 CSS라 불리는 SASS를 지원한다.

그 외에 Ruby를 사용해 본 적이 없어도 인스톨과 사용에 문제가 없으며, 테마를 바꾸더라도 포스트(마크다운 파일)만 옮겨서 수정하면 되는 등 사용법이 간단하다는 특징이 있다.

여러가지 테마가 있기 때문에 곧바로 설치가 가능하다. 커스텀 테마도 만드는 것이 가능하다.

다양한 플러그인을 지원한다. 대표적으로 jekyll-paginate가 있는데, 블로그에서 자주 보이는 페이지네이터 기능을 구현시켜준다.

또한 블로그 내 포스트 검색 기능을 위해 jekyll 전용 Algolia를 이용할 수 있으며, 댓글 기능을 위해 DISQUS를 이용할 수도 있다.

--------------
## Jekyll 시작하기
[Jekyll 학습하기](https://jekyllrb-ko.github.io/)
