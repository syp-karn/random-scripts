# Wifi login script for Linux users
#!/bin/bash

url="https://10.0.112.2:8090/login.xml"

# Set your wifi login credentials
username=""
password=""
mode="191"

curl -k -X POST "$url" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Origin: https://10.0.112.2:8090" \
  -H "Referer: https://10.0.112.2:8090/httpclient.html" \
  --data "mode=$mode&username=$username&password=$password"
