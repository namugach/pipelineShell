#!/bin/bash

# config.sh 소스하여 환경 변수 설정
source "/home/ubuntu/run/config.sh"


# 각 서버별 스크립트 경로
scripts=(
    "/home/ubuntu/run/docker/container/server1.sh"
    "/home/ubuntu/run/docker/container/server2.sh"
    "/home/ubuntu/run/docker/container/server3.sh"
)

# 각 서버에서 Docker 컨테이너 실행
for i in "${!scripts[@]}"; do
    script_path="${scripts[$i]}"
    # 스크립트 파일에서 내용 읽기
    script_content=$(cat "$script_path")

    # 내용에 변수 치환
    echo "============== $(basename "$script_path") 시작 시도 중 =============="
    echo "$script_content" | envsubst
    echo
done
