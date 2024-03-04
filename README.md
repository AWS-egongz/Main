## 🙌  이공즈 프로젝트
- **에브리타임 챗봇 & 강의 검색 엔진** 서비스입니다!
- **AWS** 와 **Elasticsearch**를 활용하여 개발하였습니다. 
- 비영리 프로젝트입니다.
## 🙌 AWS 활용
   **Product in AWS: C9, EC2, Lambda, VPC**
  
## 에브리타임 챗봇?
- 데이터 수집?
  >  연세대학교 컴퓨터과학과 게시판 정보들을 수집하였습니다.   
  >  EC2에서 매일 자정에 수집을 진행했습니다. 
  >  EC2 Turn On/Off Lambda를 만들어 사용했습니다. (불필요한 컴퓨팅 비용 없애기!)
  >  수집한 데이터는 텍스트 임베딩 모델 KR-SBERT을 거쳐 벡터화된 데이터를 저장하였습니다. 
  >  
- 챗봇의 대답?
  > 기존의 LLM (챗지피티)에 Elasticsearch 검색을 더한 Rag 기법을 사용하였습니다.  
  >  질문 쿼리를 벡터화한 후에 소스 데이터와 유사도를 비교하여 상위 10개의 데이터를 챗지피티에 주어 대답을 생성하였습니다. 
  > 유사도는 각 벡터간의 각도를 기준으로 측정하였습니다.


## 강의 검색 엔진
- Feature
  >   사용자의 쿼리가 변할 때마다 실시간 검색이 가능합니다.
  > >  어떻게 ?  👉 데이터 색인 시에 Elasticsearch 내에 Edge-Ngram 기능을 사용하여 토크나이징을 진행했습니다.

  >  한국어 강의, 동영상 강의 등 여러 조건으로 필터링이 가능합니다. (필터링 확장 가능)  

## More
-  선택한 강의들을 한눈에 볼 수 있는 시간표 UI를 사용하실 수 있습니다. 
![onealog](/시간표.png)
![onealog](/메인페이지.png)   
