Building a Test Container for Practice, Testing, and Learning

RUNNING A PRE-BUILT SAMPLE CONTAINER
Docker hosts a "getting started" image for users to play with. Run our fork of Docker's getting started image (our fork adds CORS headers so our tests can connect)

Run this command on your CLI:

docker run -d -p 80:80 allanl95/getting-started-bootdotdev:latest
Copy icon
Be sure to give it a bit of time to download the image, because you probably don't already have it stored locally.

You should see the container running in the "Containers" tab of Docker Desktop. Next, run:

docker ps
Copy icon
This will list running containers in your command line. On one of the columns you should see this:

PORTS
0.0.0.0:80->80/tcp
Copy icon
This is saying that port 80 on your local "host" machine is being forwarded to port 80 on the running container. Port 80 is conventionally used to indicate HTTP web traffic. Navigate to http://localhost:80 and you should get a webpage describing the container you're running!



# Testing the Container

Run the HTTP tests against your getting started container on http://localhost:80

Testing the following HTTP requests:

1. GET /
1. Expecting status code: 200
2. Expecting body to contain: <html
3. Expecting body to contain: Getting Started with Docker
4. Expecting body to contain: </html>


I created a bash script to run these tests for you. Run the following command in your CLI:

```
chmod +x filename.sh 
./filename.sh
```

# Implementation

This `curl` command makes a request to `http://localhost:80` and prints the HTTP status code of the response. Here's what each option does:

- `-s`: This is the "silent" mode. It means that `curl` will not show progress meter or error messages.

- `-o /dev/null`: This redirects the output (the body of the response) to `/dev/null`, effectively discarding it. `/dev/null` is a special file that discards all data written to it.

- `-w "%{http_code}"`: This uses `curl`'s `-w` or `--write-out` option to output information on stdout after a completed operation. The `"%{http_code}"` part is a variable that gets replaced with the HTTP status code of the response.

So, this command makes a request to `http://localhost:80`, discards the response body, and prints the HTTP status code. It's a way to check if a web server is responding and what status code it's returning, without displaying the response body.

