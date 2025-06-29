sudo docker compose stop 
sudo docker compose rm -v
sudo docker volume ls -qf dangling=true | xargs sudo docker volume rm
sudo docker compose up -d
sudo docker ps