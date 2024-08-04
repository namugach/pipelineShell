#!/bin/bash

# config 파일에서 값을 읽고 변수를 설정하는 함수
load_config() {
	CONFIG_FILE="../config"

	# config 파일의 내용을 읽어서 주석이 아닌 줄만 처리합니다.
	grep -v '^\s*#' "$CONFIG_FILE" | while IFS=' ' read -r name ip port; do
		case $name in
			server1)
				export SERVER1_IP=$name
				export SERVER1_IP=$ip
				export SERVER1_PORT=$port
				;;
			server2)
				export SERVER2_IP=$name
				export SERVER2_IP=$ip
				export SERVER2_PORT=$port
				;;
			server3)
				export SERVER3_IP=$name
				export SERVER3_IP=$ip
				export SERVER3_PORT=$port
				;;
		esac
	done
}
