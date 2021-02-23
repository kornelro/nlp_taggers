docker pull djstrong/krnnt

docker run -p 9003:9003 -it djstrong/krnnt:latest bash -c "cd /home/krnnt/krnnt/ && ./start_gunicorn_server.sh"