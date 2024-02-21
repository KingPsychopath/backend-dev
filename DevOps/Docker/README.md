# Docker Study Materials

This directory contains all my study materials for Docker. It includes Dockerfiles, scripts, and notes on Docker concepts, commands, and best practices.

# What is Docker?

Docker is a platform that simplifies software development by allowing developers to package their applications with all of their dependencies into a standardized unit called a container.

## Usage

Each subdirectory in this directory corresponds to a different type of material (Dockerfiles, scripts, or notes). Inside each subdirectory, you'll find relevant files and a `README.md` file with more information.

## Docker Topics Covered

These materials cover a range of Docker topics, including but not limited to:

- Docker Images and Containers
- Dockerfile Syntax and Best Practices
- Docker Compose
- Docker Networking
- Docker Volumes

## Docker Terminology

### Three Key Concepts
- **Image**: A Docker image is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform. It provides a convenient way to package up applications and preconfigured server environments.

- **Container**: A Docker container is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

- **Docker Volume**: A Docker volume is a directory on disk or in another container. Volumes are used to persist data generated by and used by Docker containers.

## Contents

- **Dockerfiles**: This folder contains Dockerfiles for building various types of Docker images.
- **Scripts**: This folder contains scripts for automating tasks with Docker.
- **Notes**: This folder contains notes on Docker concepts, commands, and best practices.

## Basic Docker Commands

- `docker run <image>`: This command is used to start a new container from an image.

- `docker build -t <image-name> .`: This command is used to build an image from a Dockerfile. The `-t` flag lets you tag your image with a friendly name.

- `docker ps`: This command is used to list all running containers.

- `docker stop <container-id>`: This command is used to stop a running container.


## Contributing

This is a personal study repository so I'm not currently accepting contributions. However, if you find any errors or have any suggestions, feel free to open an issue.

## License

This project is licensed under the terms of the MIT license.