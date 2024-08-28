# Kafka 기반 데이터 파이프라인 예제

---

## 1. 개요

**작성자:** namugach

**GitHub:** https://github.com/namugach

**메일:** namugach@gmail.com

본 프로젝트는 Docker Compose를 사용하여 Kafka 클러스터를 구축하고, 간단한 데이터 파이프라인을 구현하는 예제입니다. ZooKeeper를 사용하여 3개의 Kafka 브로커로 구성된 클러스터를 설정하고, CSV 파일의 데이터를 Kafka 토픽으로 전송하여 MySQL 데이터베이스에 저장하는 과정을 보여줍니다. 이는 데이터 파이프라인의 기본적인 구성 요소들을 보여주는 최소 단위의 예제로, 실제 데이터 파이프라인 구축을 위한 기초적인 이해를 제공합니다.


## 2. 기능

*   **Docker Compose 기반 Kafka 클러스터 구축:**  `docker-compose.yml`  파일을 사용하여 ZooKeeper와 Kafka 브로커를 컨테이너로 실행하여 클러스터를 쉽게 설정하고 관리합니다.
*   **SSH 기반 서버 관리:** Python 스크립트에서  `paramiko`  라이브러리를 사용하여 SSH를 통해 각 서버에 접속하고 명령을 실행하여 클러스터를 제어합니다.
*   **클러스터 상태 확인:**  `check_cluster.sh`  스크립트를 통해 각 서버의 ZooKeeper 및 Kafka 연결 상태를 확인합니다.
*   **클러스터 시작 및 중지:**  `start_cluster.sh`  및  `stop_cluster.sh`  스크립트를 사용하여 클러스터를 쉽게 시작하고 중지할 수 있습니다.
*   **데이터 파이프라인 구현:**
*   **데이터 수집:** Python 스크립트를 통해 CSV 파일에서 데이터를 읽어와 Kafka 토픽으로 전송합니다.
*   **데이터 전송:** Kafka를 사용하여 데이터를 안정적으로 브로커 노드들에 분산하여 전송합니다.
*   **데이터 저장:** Python 스크립트에서 Kafka 토픽의 데이터를 소비하여 MySQL 데이터베이스에 저장합니다.
*   **클러스터 설정 업데이트:**  `update_cluster_configs.sh`  스크립트를 사용하여 클러스터 구성 파일을 업데이트할 수 있습니다.
*   **실시간 모니터링:**  `monitor.sh`  스크립트를 통해 각 서버의 Kafka 토픽 소비 상태를 실시간으로 모니터링합니다.

---

## 3. 설치 및 실행

### 3.1. 사전 준비

1. **Docker 및 Docker Compose 설치:**  https://docs.docker.com/get-docker/  에서 Docker 및 Docker Compose를 설치합니다.
2. **Python 3.7 이상 설치:**  https://www.python.org/downloads/  에서 Python을 설치합니다.

### 3.2. 클러스터 설치 및 실행

1. 프로젝트 루트 디렉토리에서  `install.sh`  스크립트를 실행합니다.

```sh
./install.sh
```

2. 클러스터가 정상적으로 실행되었는지 확인합니다.

```sh
docker compose ps
```

### 3.3. 클러스터 관리

*   **클러스터 상태 확인:**

```sh
./src/run/kafka/check_cluster.sh
```

*   **클러스터 중지:**

```sh
./src/run/kafka/stop_cluster.sh
```

*   **클러스터 시작:**

```sh
./src/run/kafka/start_cluster.sh
```



### 3.4. 실시간 모니터링

1. `src/test/monitor.sh`  스크립트를 실행하여 Kafka 토픽 소비 상태를 실시간으로 모니터링합니다.

```sh
./src/test/monitor.sh
```


### 3.5. 데이터 생성 및 MySQL 연동

1. `src/test/data.csv`  파일에 데이터를 준비합니다.
2. `src/test/main.sh`  스크립트를 실행하여 데이터를 Kafka 토픽으로 생성하고 MySQL 데이터베이스에 저장합니다.

```sh
./src/test/main.sh
```


### 3.6. 클러스터 제거

1. 프로젝트 루트 디렉토리에서  `uninstall.sh`  스크립트를 실행합니다.

```sh
./uninstall.sh
```

---

## 4. 파일 구조

```
.
├── config
│   ├── api_keys
│   │   └── google.py
│   ├── config.py
│   └── requirements
│       ├── install.sh
│       └── requirements.txt
├── docker-compose.yml
├── install.sh
├── main.py
├── res
│   └── url
│       ├── list.json
│       ├── list_form.json
│       ├── list_proto.json
│       └── list_test.json
├── run.sh
├── src
│   ├── ai
│   │   ├── chat_gpt
│   │   │   └── opnai.py
│   │   └── gemini
│   │       ├── gemini.py
│   │       └── model_type.py
│   ├── prompt
│   │   ├── img_to_text_parser
│   │   │   ├── eng.md
│   │   │   └── kor.md
│   │   ├── json_converter
│   │   │   ├── eng.md
│   │   │   └── kor.md
│   │   └── string
│   │       └── kor.md
│   ├── screenshot
│   │   ├── petter.py
│   │   ├── prop.py
│   │   └── selenium.py
│   ├── run
│   │   ├── config
│   │   │   └── config.py
│   │   ├── kafka
│   │   │   ├── check_cluster.py
│   │   │   ├── check_cluster.sh
│   │   │   ├── check_conn.sh
│   │   │   ├── start_cluster.py
│   │   │   ├── start_cluster.sh
│   │   │   ├── start_server.sh
│   │   │   ├── start_zookeeper.sh
│   │   │   ├── stop_cluster.py
│   │   │   ├── stop_cluster.sh
│   │   │   ├── stop_server.sh
│   │   │   ├── update_cluster_configs.py
│   │   │   └── update_cluster_configs.sh
│   │   └── ssh
│   │       └── check.sh
│   │           └── util.py
│   └── test
│       ├── data.csv
│       ├── main.py
│       ├── main.sh
│       ├── monitor.py
│       └── monitor.sh
└── uninstall.sh

```

---

## 5. 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 
