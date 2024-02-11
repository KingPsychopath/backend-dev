# BUILDING IMAGES

I've used Docker in the past to install third-party software; both on my local machine and on the production servers of companies I've worked for. However, as a back-end developer, I've more often used it to build images of _my_ software.

## DOCKERFILES

> Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
> 
> -- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

Dockerfiles are _amazing_ because they allow us to define the environment our applications are meant to use _in code_. We can even commit the Dockerfiles to Git alongside our source code.

## CREATING A DOCKERFILE

Create a single file called `Dockerfile` in your working directory. If you're using VS Code, I'd recommend installing the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker). It will give you some nice syntax highlighting among other features.

Inside the Dockerfile add these lines of text:

```dockerfile
# This is a comment

# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# execute the 'echo "hello world"'
# command when the container runs
CMD ["echo", "hello world"]
```

Build a new image from the Dockerfile:

```bash
docker build . -t helloworld:latest
```

_`-t helloworld:latest` tags the image with the name "helloworld" and the "latest" tag. Names are used to organize your images, and tags are used to keep track of different [versions](https://en.wikipedia.org/wiki/Software_versioning)._

Run your image in a new container:

```bash
docker run helloworld
```

If all went well, you'll see "hello world" printed to the console!

Next, run `docker ps`. **You'll notice that your container isn't running anymore! All it did was print and exit. Just like regular programs, docker containers can execute simple commands that exit quickly, or they can execute servers that run until killed.**

You can see the stopped container by running `docker ps -a`. Feel free to delete the Dockerfile, we don't need it anymore.

# Why DockerFile

By default, Docker looks for a file named "Dockerfile" to build an image. The name "Dockerfile" is not arbitrary but a convention. It's the default and the most recognized naming scheme.

However, you're not strictly bound to this default. You can use a different file by specifying it with the `-f` or `--file` option in the `docker build` command.

For example, if your file is named "MyDockerfile", you would use the command:

```bash
docker build -f MyDockerfile . -t helloworld:latest
```

Just remember, if you use non-standard names, it might lead to confusion for others not familiar with your project's conventions.
