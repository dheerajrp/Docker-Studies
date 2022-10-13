### Create a hello world fastapi application. Create a Dockerfile for your fastapi hello world application. Build Docker image using Docker file. Run docker image build in previous step. Push your Docker image to Docker Hub.

#### Docker pull command
    docker pull dhee1006/hi-world

#### Docker run command
    docker run -d -p 5000:8000 dhee1006/hi-world

#### Endpoints

http://127.0.0.1:5000/docs   - Documentation

http://127.0.0.1:5000        - Hello World

http://127.0.0.1:5000/numpy  - prints numpy version

http://127.0.0.1:5000/pandas - prints pandas version

Docker image in docker hub: https://hub.docker.com/repository/docker/dhee1006/hi-world
