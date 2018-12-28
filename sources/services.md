# Using services and systemd

## General

There is system for controlling services (programs ran in background independently on users) named *systemd* and helper for it *systemctl*. They helps to keeps list of system services and manage their start, stop and status. Also they helps to automatically start needed services

## Configuring

To keep the track of services systemd uses *.service* files located in */lib/systemd/system* dir or in */lib/systemd/network* dir. To add new service place *.service* file with the name of new service in this folder.

Example *serviio.service*:

```
[Unit]
Description=DLNA server
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/sbin/runuser -l ubuntu -c"/media/services/serviio/bin/serviio.sh &"
ExecStop=/sbin/runuser -l ubuntu -c"/media/services/serviio/bin/serviio.sh -stop &"

[Install]
WantedBy=multi-user.target
```

## Usage

### Enable autostart

```
sudo systemctl enable serviio
```

NOTE: This will create symlink for the service in */etc/systemd/wanted* directory

### Manually start/stop service

```
sudo systemctl start/stop serviio
```

NOTE: For this action config should have *ExecStart*/*ExecStop* value

### Get service status

```
systemctl status serviio
```

NOTE: In case starting script is used for only starting application and the quits with some code status of the service will be *inactive(dead)* with status code. This is OK and doesn't mean that service not run or failed

[Back](docs.html)
