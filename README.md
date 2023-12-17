# observeshop-custom-loadgen

## Pushing CDP update

Add the following to user crontab

```
0 * * * * /home/max/locust/.venv/bin/python3 /home/max/locust/pushdata.py  /home/max/locust/people.json
```

## Running locust loadgen interactively

```
locust --host https://www.observeshop.com --users 40 --autostart
```

## Runing locust loadgen as a systemd service

Create a wrapper script, so we can run this from venv `/home/max/locust/service-run.sh`:

```
#!/usr/bin/env bash
set -e
source "/home/max/locust/.venv/bin/activate"
cd /home/max/locust/
locust --host https://www.observeshop.com --users 40 --autostart
```

Create systemd unit file `/etc/systemd/system/locust.service`

```
[Unit]
Description=Locust load generator for observeshop.com
After=multi-user.target
[Service]
Type=simple
Restart=always
/home/max/locust/service-run.sh
[Install]
WantedBy=multi-user.target
```

Enable and run the service

```
sudo systemctl daemon-reload
sudo systemctl enable locust.service
sudo systemctl start locust.service
```

Validate service is working

```
sudo systemctl status locust.service

● locust.service - Locust load generator for observeshop.com
     Loaded: loaded (/etc/systemd/system/locust.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-12-17 18:31:43 UTC; 1min 31s ago
   Main PID: 4013 (bash)
      Tasks: 2 (limit: 9389)
     Memory: 66.7M
        CPU: 5.002s
     CGroup: /system.slice/locust.service
             ├─4013 bash /home/max/locust/service-run.sh
             └─4014 /home/max/locust/.venv/bin/python3 /home/max/locust/.venv/bin/locust --host https://www.observeshop.com --users 40 --autostart

Dec 17 18:31:43 europa systemd[1]: Started Locust load generator for observeshop.com.
Dec 17 18:31:43 europa service-run.sh[4014]: [2023-12-17 18:31:43,998] europa/INFO/locust.main: Starting web interface at http://0.0.0.0:8089
Dec 17 18:31:44 europa service-run.sh[4014]: [2023-12-17 18:31:44,003] europa/INFO/locust.main: Starting Locust 2.20.0
Dec 17 18:31:44 europa service-run.sh[4014]: [2023-12-17 18:31:44,003] europa/INFO/locust.main: No run time limit set, use CTRL+C to interrupt
Dec 17 18:31:44 europa service-run.sh[4014]: [2023-12-17 18:31:44,005] europa/INFO/locust.runners: Ramping to 40 users at a rate of 1.00 per second
Dec 17 18:32:23 europa service-run.sh[4014]: [2023-12-17 18:32:23,047] europa/INFO/locust.runners: All users spawned: {"WebsiteUser": 40} (40 total users)
```
