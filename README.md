\# Dockerized Flask Web Application



> \*\*Status:\*\* ✅ Completed  

> \*\*Project Type:\*\* DevOps / Docker Fundamentals  

> \*\*Focus:\*\* Containerization, Docker Networking, Linux, and Reproducible Deployments



\## Project Overview



This project demonstrates how to containerize a Python Flask web application using Docker. The application is packaged into a Docker image containing the application code, runtime environment, and required dependencies, allowing it to run consistently across different systems.



The primary goal of this project was to develop a practical understanding of Docker and the engineering principles behind containerization. Rather than simply learning Docker commands, I focused on understanding concepts such as image creation, container lifecycle management, dependency management, reproducible builds, and container networking. Throughout the project, I also strengthened my Linux fundamentals and gained hands-on experience deploying a containerized web application.



\## Objectives



\- Containerize a Python Flask web application using Docker.

\- Learn how Docker images and containers are created and managed.

\- Understand Dockerfile instructions and the image build process.

\- Explore dependency management using `requirements.txt`.

\- Configure container networking using Docker port mapping.

\- Strengthen Linux command line skills while working in a cloud virtual machine.

\- Develop a deeper understanding of reproducible deployments.



\## Project Architecture



```text

&#x20;               Browser

&#x20;                   │

&#x20;                   ▼

&#x20;        http://VM\_IP:8080

&#x20;                   │

&#x20;                   ▼

&#x20;         Host Port (8080)

&#x20;                   │

&#x20;                   ▼

&#x20;    Docker Port Mapping (-p)

&#x20;                   │

&#x20;                   ▼

&#x20;     Container Port (5000)

&#x20;                   │

&#x20;                   ▼

&#x20;       Flask Application

&#x20;                   │

&#x20;                   ▼

&#x20;            HTTP Response

```



The browser sends an HTTP request to the virtual machine through the host port. Docker forwards the request to the mapped container port, where the Flask application processes it and returns the response back to the browser. This demonstrates how Docker isolates applications while still allowing controlled communication through port mapping.



\## Technologies Used



| Technology | Purpose |

|------------|---------|

| Python 3 | Backend programming language |

| Flask | Web application framework |

| Docker | Application containerization |

| Linux Ubuntu | Development environment |

| Git and GitHub | Version control and project hosting |

| Google Cloud Platform | Virtual machine hosting |



\## Repository Structure



```text

.

├── app.py

├── Dockerfile

├── requirements.txt

├── README.md

└── screenshots/

&#x20;   ├── 01-source-code.png

&#x20;   ├── 02-dockerfile.png

&#x20;   ├── 03-project-files-created.png

&#x20;   ├── 04-docker-image-build.png

&#x20;   ├── 05-docker-image-built.png

&#x20;   ├── 06-running-container.png

&#x20;   ├── 07-localhost-curl-test.png

&#x20;   ├── 08-gcp-firewall-rule-port-5000.png

&#x20;   ├── 09-web-app-browser-test.png

&#x20;   └── 10-final-project-directory.png

```



\## Dockerfile Breakdown



| Instruction | Purpose |

|------------|---------|

| `FROM python:3.11` | Uses the official Python base image as the runtime environment. |

| `WORKDIR /app` | Sets the working directory inside the container. |

| `COPY . .` | Copies the application files into the container image. |

| `RUN pip install -r requirements.txt` | Installs required Python dependencies during the image build. |

| `EXPOSE 5000` | Documents that the application listens on port 5000. |

| `CMD \["python", "app.py"]` | Starts the Flask application when a container is launched. |



\## Build and Run



Build the Docker image:



```bash

docker build -t flaskapp .

```



Run the container:



```bash

docker run -d -p 8080:5000 flaskapp

```



Open the application:



```text

http://<VM\_IP>:8080

```



\## Skills Demonstrated



\- Docker image creation and container deployment

\- Writing and understanding Dockerfiles

\- Python Flask application deployment

\- Dependency management using `requirements.txt`

\- Docker container networking and port mapping

\- Linux command line fundamentals

\- Cloud VM deployment on Google Cloud Platform

\- Basic firewall configuration for web applications

\- Git and GitHub version control

\- Technical documentation and project organization



\## Project Walkthrough



\### 01 Source Code



!\[Source Code](screenshots/01-source-code.png)



\### 02 Dockerfile



!\[Dockerfile](screenshots/02-dockerfile.png)



\### 03 Project Files Created



!\[Project Files Created](screenshots/03-project-files-created.png)



\### 04 Docker Image Build



!\[Docker Image Build](screenshots/04-docker-image-build.png)



\### 05 Docker Image Built



!\[Docker Image Built](screenshots/05-docker-image-built.png)



\### 06 Running Container



!\[Running Container](screenshots/06-running-container.png)



\### 07 Localhost Curl Test



!\[Localhost Curl Test](screenshots/07-localhost-curl-test.png)



\### 08 GCP Firewall Rule



!\[GCP Firewall Rule](screenshots/08-gcp-firewall-rule-port-5000.png)



\### 09 Browser Test



!\[Browser Test](screenshots/09-web-app-browser-test.png)



\### 10 Final Project Directory



!\[Final Project Directory](screenshots/10-final-project-directory.png)



\## Key Learning Outcomes



This project helped me move beyond simply running Docker commands and develop a deeper understanding of the engineering principles behind containerization.



Some of the key concepts I learned include:



\- The difference between Docker images and containers

\- Building reproducible environments using Dockerfiles

\- Managing application dependencies during the image build process

\- Understanding build context and the Docker image lifecycle

\- Configuring Docker networking through host and container port mapping

\- Understanding how browser requests travel through the host, Docker, and the running container

\- Strengthening Linux fundamentals while working in a cloud environment



\## Reflection



Before starting this project, Docker mostly felt like a tool that could package applications. By the end of the project, I understood the reasoning behind many of Docker's design decisions, including why images are built before containers run, why dependencies are installed during the build process, and how Docker networking allows isolated applications to communicate through controlled port mapping.



One of the biggest takeaways from this project was learning to think beyond individual commands and instead understand the engineering principles behind containerization. That shift in thinking has given me much more confidence as I continue learning Linux, DevOps, cloud technologies, and software engineering.



\## Future Improvements



\- Deploy the application using Docker Compose

\- Containerize a multi service application

\- Integrate a reverse proxy such as NGINX

\- Deploy to a cloud container platform

\- Implement CI/CD using GitHub Actions

