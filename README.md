# Pindrop-test

### Modules Needed
```
psutil==4.2.0
Flask==0.11.1
```

### Api calls

1. Plain api call http://127.0.0.1:5000
2. Api call with date http://127.0.0.1:5000/2016-06-11
3. Api call with date and time http://127.0.0.1:5000/2016-06-11/10:10:10

### Metrics monitored

1. cpu
  1. cpu_usage
  2. cpu_times
2. disk
3. memory
  1. swap_memory
  2. virtual_memory
4. network

### Specific api calls

Get metrics about each metric
http://127.0.0.1:5000/{args}
args can be ['cpu', 'cpu/cpu_times', 'cpu/cpu_sage']
http://127.0.0.1:5000/cpu
```json
    "cpu": {
      "cpu_times": {
        "idle": 1161655.8,
        "nice": 0,
        "system": 54845.2,
        "user": 89503.77
      },
      "cpu_usage": {
        "cpu_count": 4,
        "cpu_percent": 11,
        "cpu_usage_each_core": [
          9,
          2,
          6.9,
          3
        ]
      }
    }
```

### Complete system metrics
http://127.0.0.1:5000/
```json
{
  "system_metrics": {
    "cpu": {
      "cpu_times": {
        "idle": 1161655.8,
        "nice": 0,
        "system": 54845.2,
        "user": 89503.77
      },
      "cpu_usage": {
        "cpu_count": 4,
        "cpu_percent": 11,
        "cpu_usage_each_core": [
          9,
          2,
          6.9,
          3
        ]
      }
    },
    "disk": {
      "/dev/disk0s2": {
        "free": 0,
        "percent": 100,
        "total": 184832,
        "used": 184832
      },
      "max_used": 184832
    },
    "memory": {
      "swap_memory": {
        "bytes_in": 88649940992,
        "bytes_out": 659197952,
        "free": 343932928,
        "percent": 68,
        "total": 1073741824,
        "used": 729808896
      },
      "virtual_memory": {
        "available": 2120491008,
        "free": 26714112,
        "percent": 75.3,
        "total": 8589934592,
        "used": 6086709248
      }
    },
    "network": {
      "bytes_recv": 35705422317,
      "bytes_sent": 6008628838,
      "packets_recv": 28330908,
      "packets_sent": 14335993
    }
  }
}
```

### To start the api
```shell
python app.py
```

### Creating corn job
```
* * * * * ~/Pindrop-test/schedule.sh
```
Before creating the job set the permissions of ```schedule.sh```
```chmod +x ~/Pindrop-test/schedule.sh```
