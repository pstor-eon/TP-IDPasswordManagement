# Toy Project ID Password Management

사이트마다 아이디와 비밀번호를 다르게 사용하는데 가입하는 사이트는 늘어나고 사이트마다 외울 수가 없어서 시작하게 된 토이프로젝트 입니다. 토이프로젝트로 시작했으며 부족한 점이 많이 있습니다. 또한 혼자서 공부하면서 만들고는 있지만 도움을 받고 싶습니다. 많은 기여해주시면 감사하겠습니다. 마지막으로 로컬에서 바로 실행할 수 있게 라이브러리를 최소한으로 사용하려고 합니다.

이 프로젝트는 사용자가 웹 사이트 계정 정보를 안전하게 저장하고 검색할 수 있는 간단하고 효과적인 암호 관리자입니다. 사용자는 암호화된 데이터베이스에 계정 정보를 저장하여 기밀성과 보안을 보장합니다. 이 암호 관리자는 SQLite3 데이터베이스를 사용하여 데이터를 로컬로 저장하며, 다양한 암호화 및 해시 알고리즘을 통해 사용자 및 계정 정보를 보호합니다.

### 시작하기
이 프로젝트를 시작하려면, 아래의 단계에 따라 해 주세요.

1. 이 프로젝트를 로컬 시스템에 복제합니다.
2. 프로젝트 디렉토리로 이동합니다.
3. 필요한 라이브러리를 설치합니다.
4. 프로그램을 실행합니다.

### 사용 방법
1. Python 3.x 버전이 필요합니다. 필요한 라이브러리를 설치합니다.
```python
pip install sqlite3
pip install cryptography
```
2. 파이썬을 실행합니다.
```python
python password_manager.py
```
사용자 등록 및 로그인을 합니다.

- 사용자 등록: 사용자 이름, 비밀번호 확인을 입력합니다.
- 로그인: 사용자 이름과 비밀번호를 입력합니다.
- 로그인 후, 메뉴에서 원하는 작업을 선택합니다.

- 계정 추가: 웹 사이트 이름, 계정 사용자 이름, 비밀번호를 입력합니다.
- 계정 찾기: 웹 사이트 이름을 입력하면, 해당 사이트의 계정 정보가 출력됩니다.
- 계정 삭제: 웹 사이트 이름을 입력하면, 해당 사이트의 계정 정보가 삭제됩니다.
- 작업을 완료한 후, 로그아웃하거나 프로그램을 종료합니다.

### 사용된 기술 및 라이브러리
1. SQLite3: 로컬 스토리지를 위한 경량화된 관계형 데이터베이스 관리 시스템.
2. hashlib: SHA-256 해시 알고리즘을 사용하여 사용자 및 계정 정보를 안전하게 저장.
3. cryptography: Fernet 암호화를 사용하여 데이터베이스 내의 계정 정보를 암호화.
4. getpass: 사용자로부터 비밀번호 입력을 안전하게 받기 위한 라이브러리.

### 기여 방법
이 프로젝트에 기여하고 싶으시다면, 다음의 단계를 따라 해 주세요.

1. 프로젝트를 포크합니다.
2. 새로운 기능 브랜치를 생성합니다.
3. 변경 사항을 커밋합니다.
4. 브랜치에 푸시합니다.
5. Pull Request를 생성합니다.

### 프로젝트 참여
본 프로젝트는 오픈 소스로 진행되고 있으며, 기여를 원하시는 분들은 프로젝트 저장소를 방문하여 개선 사항이나 버그 수정 등에 참여할 수 있습니다. 이 프로젝트는 많은 사용자들의 도움과 함께 발전해 나갈 것입니다. 프로젝트에 관심이 있으신 분들은 아래 방법을 통해 참여하실 수 있습니다.

1. 이슈 제기: 프로젝트 저장소의 이슈 트래커를 통해 버그, 개선 사항, 새로운 기능 제안 등을 제기하실 수 있습니다.
2. 풀 리퀘스트 제출: 프로젝트 저장소를 포크하여 개선 사항이나 버그 수정 등을 작업한 뒤, 풀 리퀘스트를 제출하여 기여하실 수 있습니다.
3. 코드 리뷰: 다른 참여자들의 풀 리퀘스트를 리뷰하거나, 토론에 참여하여 프로젝트 발전에 기여하실 수 있습니다.
4. 문서화 및 번역: 프로젝트의 사용자 가이드, 개발자 가이드 등 문서화 작업에 참여하거나, 다양한 언어로 번역을 제공하여 글로벌 사용자들에게 도움을 드릴 수 있습니다.
5. 커뮤니티 참여: 사용자 커뮤니티를 구축하고, 다양한 경험을 공유하며 프로젝트의 성장에 도움을 주실 수 있습니다.

본 프로젝트는 지속적으로 성장하고 발전하기 위해 많은 참여자들의 관심과 기여를 기다리고 있습니다. 함께 이 프로젝트를 더 나은 소프트웨어로 만들어 가는데 동참해 주시기 바랍니다.

### FAQ 및 문제 해결
프로젝트에 관한 질문이나 문의사항이 있으시면, 프로젝트 저장소의 이슈 트래커를 통해 연락주시거나 이메일로 문의주시기 바랍니다. 프로젝트 참여자들이 적극적으로 도움을 드릴 것입니다. 또한 문제가 발생하거나 질문이 있는 경우, 이슈 페이지에서 새로운 이슈를 생성하십시오. 가능한 한 빨리 답변해 드리겠습니다.

### 주의 사항
이 프로젝트는 학습 목적으로 개발되었으며, 실제 애플리케이션으로 사용하기에는 데이터 보안과 관련된 제한 사항이 있습니다. 실제 비밀번호 관리 프로그램을 사용하려면, 전문적인 솔루션을 사용하세요.

### 라이센스
이 프로젝트는 MIT 라이센스에 따라 제공됩니다. 자세한 내용은 LICENSE 파일을 참조하십시오.
