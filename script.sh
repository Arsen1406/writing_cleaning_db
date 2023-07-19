#!/bin/bash

server_file="путь/до/файла/с/хостами"
file="путь/до/файла/который/копируем"
path_in_host="/путь/для/файла/на/хосте"
email="mailbox@server.ru"
unreachable_servers=()

rm ./unreachable_servers.txt

for ip in $(cat $server_file)
  do
    status=$(ssh -o BatchMode=yes -o ConnectTimeout=5 'root'@ip echo ok 2>&1)

    if [[ $status == ok ]] ; then
      scp "$file" "root@$ip:$path_in_host"
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
else
  mail -s "Файлы успешно переданы на все адреса" "$email" < unreachable_servers.txt
fi
