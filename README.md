# 프로젝트 설명

개인 블로그 용이자 개인 피력 사이트

## 버전 변경

### 2023-06-30

- APIView => GetViewSet(list, retrieve, generic)

- methodserializer => nestserializer 형태로 변경

- test code 적용(api, service)

- 기존 post를 md 파일 혹은 html 파일을 올려 서빙하는 형태에서 자체 db로 보관하는 형태로 변경

- path -> Custom 한 router 로 변경 현재 trailish_slash가 없는 경우 detail 오류 픽스

- pydantic, dotenv 를 통한 설정 관리

- 현재 secret_key 관련 기존 private 한 환경에서는 문제없었지만 public 한 환경에서는 문제가 되어서 github 에서 filter 를 통한 settings 파일 삭제 및 개선 등록

- model verbose_name 및 구조 개선

## 설계

### 백엔드(프라이빗 프로젝트로 올림)

- 리포지토리: [https://github.com/black2st11/my_blog_backend](백엔드 리포지토리) 참고

- 언어 : Python(3.10) (기존 3.11 에서 lambda python 지원이슈로 인해 다운그레이드)

- 프레임워크 : Django

- 라이브러리 : Django Rest Framework, CORS Headers, django-storages, psycopg2-binary, s3boto, zappa, pydantic, pytest, pytest-djangom, ckeditor

- DBMS : PostgreSQL(AWS RDS)

- 배포 :
  이전(Docker + AWS ECR + ECS + Fargate + LB + ACM + Route53 + S3)
  현재 AWS에서 진행 (Lambda + API Gateway + ACM + Route53 + S3 )
  Zappa 를 이용해서 배포, AWS 문서에서 공식으로 사용하기에 사용
  변경 이유 :

  1. 비용 관련 문제
     ECS 와 Fargate를 이용 시 1미만으로 CPU와 메모리 할당이 가능해서 좋았지만 비용이 그래도 다른 서비스와 엮어져서 조금은 나오는 정도라서 지금의 서비스에서는 가성비가 안 맞다고 생각했고, 서버리스의 경우 해당하는 기능을 다 합친 상태로 존재하고 비용(100만 건당 비용 + 시간 점유 비용) 도 더 저렴하다고 판단 이전

  2. 관리 용이성
     ECS 의 경우 서비스가 커지는 순간마다 관리가 되어지는 부분이 많다고 생각했지만 Lambda 의 경우 해당 하는 부분에서 편리하기도 했으며 CI/CD 적용이 더 용이하다고 판단

  3. 생각보다 Clod Start 의 영향이 크지않은 점
     기존에는 cold start 가 유의미하게 눈에 보일 줄 알았지만 실제로 테스트하고 올린 프로젝트에서는 눈에 띄지 않는 속도였고 AWS 공식 문서에서 실제 프로덕션 상태에서 cold start로 문제를 겪는 비율이 실제 요청건의 1%미만으로 나와서 오히려 긍정적인 점으로 다가와서 적용

### 프론트(https://blog.black2st11.com)

- 리포지토리: (https://github.com/black2st11/blog_front)

### 전략

#### 초기 전략

##### 간략

프론트만으로 해당하는 프로젝트를 구성 및 배포 할 예정이었음

##### 페이지 구성

- 메인(한번에 보는 용도)

- 소개 페이지(개인 정보 관련 나열)

- 경력(경력 사항 나열)

- 경험(프로젝트 위주로 나열)

##### 문제점

경력 수정이 필요할 때마다 번거롭게 코드 수정 및 데이터 추가가 코드내에서 이뤄져야함

기능에 대한 부분이 프론트에서만 해야하다보니 제한이 되어짐

####

#### 현재 전략

##### 간략

프론트와 백엔드를 구성 프론트에서는 데이터를 보여주는 역할을 담당
백엔드의 경우 데이터 서빙 및 계산 관련(경력 계산 및 프로젝트 기간 계산) + 어드민 페이지를 통한 DB 데이터 삽입

##### 페이지 구성

- 메인(한번에 간략하게 보는 용도, 현재 각각 페이지에 해당하는 최대 3개의 콘텐츠만 보여줌)

- 소개 페이지(개인 정보 관련 나열)

- 경력(경력 사항 나열)

- 경험(프로젝트 위주로 나열)

- 던전? (업무 진행 시 어려웠던 부분 나열)

- 공략(공부했던 부분을 나열)

- 메시지(Q&A 형식으로 메시지를 받으면 답장해주는 형식)

##### 세부 기능

- ~~공략 : 작성해놓은 md 파일을 => html 파일로 변환 S3에 저장 후 URL을 전송 해당하는 부분을 페이지내에서 보여주는 형식~~(deprecated)

- 메시지 : 대댓글 형식으로 답변(댓글을 0으로 가정 후, 뎁스는 1번 대댓글 하나) + 하루에 IP 관련으로 해서 5회 초과 등록 불가

- 계산 관련 : 기간이 기입되어 있는 부분은 계산을 통해서 개월 수로 변환
