# Headless Test & VNC environment

### Download RealVNC viewer:

You can download the [real-vnc](https://www.realvnc.com/en/connect/download/viewer/macos/). and Install as per your\
operating system.

##Running docker image
####  Step 1:
For the Debugging we should require the Docker Selenium WebDriver Image with VNC server.So First Step is to build the \
docker file
```sh
$ docker build -t <image name:tag> -f chrome-debug .
```

#### Step 2:
the following step mounts the volume to the desired location within the container using -v. Also to get the ports to \
link container with VNC server
  
```sh
$ docker run -v C:/Users/:/dev/smh/ <image name:tag>
```

#### Step 3:
After running the Docker container we should verify the Container Process and Port Details.
```sh
$ docker ps
```

##Starting VNC and create VNC
####Step 1: 
Open real VNC viewer downloaded in the previous Steps.

####Step 2: 
From File Menu select: Create New Connection

####Step 3: 
Enter Value of VNC Server as localhost:\
VNC server: 


## Running Tests

By default, example tests are configured to run in chrome locally, so chrome must be installed in your machine and the chrome driver must be downloaded and configured: Download 
- Download [chromedriver_*.zip](https://chromedriver.chromium.org/downloads)
- Unzip file and save the executable in a local folder
- Configure driver path in [Driver] section in conf/properties.cfg file
    ```sh
    [Driver]
    chrome_driver_path: C:\Drivers\chromedriver.exe
    ```
    
To Run all tests:
```sh
$ behave
```

To Run a single test:
```sh
$ behave --tags=@CreateAccount
```
