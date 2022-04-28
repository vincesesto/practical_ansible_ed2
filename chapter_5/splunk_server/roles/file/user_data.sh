#!/bin/bash
set -e -x
wget -O splunk-8.0.5-a1a6394cc5ae-linux-2.6-x86_64.rpm 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=8.0.5&product=splunk&filename=splunk-8.0.5-a1a6394cc5ae-linux-2.6-x86_64.rpm&wget=true'
rpm -i splunk-8.0.5-a1a6394cc5ae-linux-2.6-x86_64.rpm
sleep 30
sudo -u splunk /opt/splunk/bin/splunk start  --answer-yes --no-prompt --accept-license  --seed-passwd newpassword
