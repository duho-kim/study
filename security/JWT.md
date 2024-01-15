> 프로젝트 진행 당시 회원가입/로그인 기능을 Session을 사용해서 구현했다.<br>
> JWT도 사용해보고 싶었기에 공부해볼까?


## JWT(Json Web Token) 란?<br>
- 인증에 필요한 정보를 암호화시킨 토큰
- JSON 객체를 사용하여 데이터 전달
- RESTful API와 같은 Stateless 환경에서 데이터를 주고받을 수 있음
- 웹 표준을 따르기 때문에 대부분의 언어가 지원
<br><br>

## JWT(Json Web Token) 구조<br>
![JWT구조](https://github.com/duho-kim/study/assets/155808974/1dfd7bf8-441e-44b7-b954-85ac4c5dd937)
*- JWT.io 사이트 캡쳐*

- 위 사진과 같이 Header.Payload.Signature로 구성되어 있으며 각 부분은 점(.)으로 구분

### (1) Header
- 헤더에서는 서명 키 식별값, 해시 알고리즘, 토큰의 타입을 정의할 수 있다
- kid : 서명 시 사용하는 키(Public/Private Key)를 식별하는 값
- alg : HS256(HMAC SHA-256), HS512, RS256(RSASSA SHA-256), ES256(ECDSA P-256 curve SHA-256)
- typ : 토큰 타입

### (2) Payload(Data)
- 토큰에서 사용하는 정보 클레임(Claim)이 담긴다
- Claim은 사용자가 원하는 Key와 Value로 구성
- registered, public, private 세가지 종류로 나뉨

  #### 1. registered claim : 등록된 클레임
  - registered claim 종류 : https://datatracker.ietf.org/doc/html/rfc7519#section-4.1

  #### 2. public claim : 공개 클레임
  - 발행자가 임의로 정의 가능
  - 충돌 방지를 위해 Registered claim과 같은 내용을 쓰지 않도록 주의
  - 중복되지 않는 내용이 포함될 수 있는 URI 사용
  - https://www.iana.org/assignments/jwt/jwt.xhtml 참조
  
  #### 3. private claim : 비공개 클레임
  - 발행자와 사용자가 서로 정보를 공유하기 위해 커스터마이징된 클레임
  - Registered나 Public에 포함되지 않는 항목이어야 한다
  
### (3) Signature
- 서버 측에서 관리하는 비밀키가 유출되지 않는 이상 복호화할 수 없어서, payload에 저장된 값이 위변조 되었는지 확인할 때 사용
- header와 payload의 base64 인코딩값을 secrect값과 함께 해쉬값을 만들어냄(비밀코드)

## JWT(Json Web Token) 장단점<br>

### 장점
- Stateless
- 확장성이 뛰어나다(서버를 여러대 사용해도 토큰만 있으면 인증 가능)
  
### 단점
- 이미 발급된 JWT를 만료시킬 방법이 없다
- 길이가 길어 인증이 필요한 요청이 많으면 서버 자원낭비 발생
- 유효기간이 끝나기 전 악의적인 탈취자에 의해 정보 유출 가능성 <br>
  AccessToken 만료시간은 짧게, RefreshToken을 이용하여 AccessToken 재발급 받는 형식으로 보완
