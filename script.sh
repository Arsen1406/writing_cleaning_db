#!/bin/bash

server="./123.txt"
file=".file"
email="mailbox@server.ru"
unreachable_servers=()

rm ./unreachable_servers.txt

for ip in $(cat $server)
  do
    status=$(ssh -o BatchMode=yes -o ConnectTimeout=5 'root'@ip echo ok 2>&1)

    if [[ $status == ok ]] ; then
      scp "$file" "root@$ip:/путь/для/файла"
    else
      unreachable_servers+=("$ip")
    fi
  done

if (( ${#unreachable_servers[@]} != 0 )); then
  for server in "${unreachable_servers[@]}";
  do
    echo "$server" >> unreachable_servers.txt;
  done
  mail -s "Недоступные серверы" "$email" < unreachable_servers.txt
fi
