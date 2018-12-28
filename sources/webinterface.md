# Webinterface

## General

Webinterface service is used for showing simple html page with urls for other services. 

## Access

To access webinterface from local network open raspberry ip (192.168.100.100) on the 8080 port

```
192.168.100.100:8080
```

## Structure

This service is implemented by using simple http server from python. 

*index.html* and run script placed in **/media/services/webinterface**

To run service manually use

```
sh start.sh
```

## Autorun

Service starts automatically on the system start using [systemd](services.html) system. Confing file located at

```
/lib/systemd/system/webinterface.md
``` 

[Back](docs.html)
