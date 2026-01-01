# setup
## MAC
brew install redis
brew services start redis
brew services info redis

## Linux
sudo apt-get install redis
sudo systemctl enable redis-server.service
sudo systemctl start redis-server

