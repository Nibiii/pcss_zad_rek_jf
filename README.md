## About The Project

The app is my recruitment assignment for junior DevOps position at PCSS. It is supposed to return IP of the requesting client. 
It should return content type based on HTTP request header (not sure i understood correctly) and also return a full list of returned IP addresses.
The app is supposed to be written in Python and run as a Docker container. Errors are handled by Flask, request frequency as well. 
Docker image contains Python-alpine image which is only ~40MB. The app also contains Kubernetes YAML file which allows for app and service deployment, and also monitoring app's health and restarting it when it returns HTTP error code.



### Built With

* [Python](https://www.python.org/)
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites


* Docker
	```
	Go to https://docs.docker.com/get-docker/, choose suitable version and install it.
	```
* kubectl
	```
	Go to https://kubernetes.io/docs/tasks/tools/, click link corresponding to your os version and follow the instructions/
	```
	
### Installation

1. Open CMD/Terminal
2. Navigate to a directory containing downloaded repository
3. Create Docker image out of the repository
	```sh
	docker build -t pcss-zad-rek-jf .
	```
	
	Very important to name the image exactly like in the example above!!! If You won't name the image like that, You will need to change the image name in .yaml file needed for Kubernetes deployment!
	
4. Deploy app in Kubernetes
   ```sh
   kubectl apply -f api-k8.yaml
   ```
5. The app is running! YEY!



### Usage
* App uses port 80 so remeber to check if there is no app already listening on this port!
* To check your IP address go to http://*server_ip_address*/ </br>
* To see list of all registered addresses go to http://*server_ip_address*/history



### TO DO(?)

* The app won't return external client's IP address (from outside of the Kubernetes LAN) 
	but I'm unsure if it's even possible with the way Kubernetes and Docker proxy their requests.
