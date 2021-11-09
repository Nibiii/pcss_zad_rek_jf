## About The Project

The app is my recruitment assignment for junior DevOps position at PCSS. It is supposed to return IP of the requesting client. 
It should return content type based on HTTP request header (not sure i understood correctly) and also return a full list of returned IP addresses.
The app is supposed to be written in Python and run as a Docker container. Errors are handled by Flask, request frequency as well. 
Docker image contains Python-alpine image which is only ~40mbs. The app also contains Kubernetes YAML file which allows for app and service deployment, and also monitoring app's health and restarting it when it returns HTTP error code.


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites


* Docker
	Go to https://docs.docker.com/get-docker/, choose suitable version and install it.
* kubectl
	Go to https://kubernetes.io/docs/tasks/tools/, click link corresponding to your os version and follow the instructions/
	
### Installation

1. Open CMD/Terminal
2. Navigate to a directory containing downloaded repository
3. Create Docker image out of the repository
	```sh
	docker build -t *image-name-here* .
	```
4. Deploy app in Kubernetes
   ```sh
   kubectl apply -f api-k8.yaml
   ```
5. The app is running! YEY!

<p align="right">(<a href="#top">back to top</a>)</p>

### TO DO(?)

* The app won't return external client's IP address (ex. from another computer in LAN) 
	but I'm unsure if it's even possible with the way Kubernetes and Docker proxy their requests.