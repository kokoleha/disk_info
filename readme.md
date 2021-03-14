1. Prometheus
   Приложение diskifo.py определяет свободное место на диске и отдает информацию в виде метрик Prometheus через встроенный http-сервер на порту 8000 (server-ip:8000/metrics).
   Метрики:
used_disk_info
size_disk_info

2. Docker
   При запуске в контейнере необходимо примонтировать нужные для отслеживания диски, чтобы диски были видны изнутри контейнера.
   Cборка образа из Dockerfile в текущей директории: 
docker build -t kokoleha/diskinfo .   	
   запуск контейнера из образа kokoleha/diskinfo:
docker run -it -p 8000:8000 kokoleha/diskinfo

3. Jenkins
   Для запуска Jenkinsfile необходим плагин pipeline для jenkins.
   Тест test.py првоеряет работу http сервера.
   Pipeline SCM from Git: 
https://github.com/vutracer/disk_info/

4. Kubernetes 
   запуск Helm-chart:
helm install diskinfo ./DiskinfoChart
