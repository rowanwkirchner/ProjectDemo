# Automation project

# Project Scope
Automating of a clothing website called 'Your Laga", showing how user interactions will happen. The automation Process includes:

    - Creating a new account and Registering a customer
    - Login in with exisiting user credentials(using positive - and negative process)

## Getting Started

The requirements to install Toolium are Python 3.7 and pip.
Clone projectDemo repository and install requirements. It's highly recommendable to use a virtualenv.
### Prerequisites
the following is required to be installed to run the project
```sh
$ git clone https://github.com/SinawoHlaleleni/ProjectDemo.git
$ cd ProjectDemo
$ pip install pipenv
$ pipenv shell
$ pip install -r requirements.txt
```


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
