# msi3

### How to run

``` bash
docker build -t localhost:32000/web:v1 . 
docker push localhost:32000/web:v1
  
k apply -f app-deployment.yaml
k apply -f app-service.yaml
k apply -f db-deployment.yaml
k apply -f db-service.yaml
k apply -f cache-deployment.yaml
k apply -f cache-service.yaml
k apply -f pv.yaml
k apply -f pvc.yaml
k apply -f ingress.yaml

curl app.127.0.0.1.xip.io/about 
```


### Rolling update 

![alt text](https://github.com/zspiler/msi3/blob/master/screenshots/rolling1.png?raw=true)
![alt text](https://github.com/zspiler/msi3/blob/master/screenshots/rolling2.png?raw=true)

### Blue/green 

![alt text](https://github.com/zspiler/msi3/blob/master/screenshots/bluegreen1.png?raw=true)
![alt text](https://github.com/zspiler/msi3/blob/master/screenshots/bluegreen2.png?raw=true)
