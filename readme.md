1.Приложение diskifo.py определяет свободное место на диске и отдает информацию в виде метрик Prometheus через встроенный http-сервер на порту 8000 (server-ip:8000/metrics). При запуске в контейнере необходимо примонтировать нужные для отслеживания диски в контейнер, чтобы диски были видны изнутри контейнера.  Метрики:
used_disk_info
size_disk_info

-сборка образа из Dockerfile в текущей директории:
docker build -t kokoleha/diskinfo .   	

-запуск контейнера из образа kokoleha/diskinfo:
docker run -it -p 8000:8000 kokoleha/diskinfo

3. Jenkins использует плагин pipeline
4. Kubernetes Helm-chart
