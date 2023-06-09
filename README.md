# gym-tracker - Gym Member/Guest Management System

## Requirements To Run

    Docker / Docker Compose
    Kubernetes
    Python
    Pip

## Steps to Run

### 1. Download the project
  
    git clone https://github.com/cs5573-Group12/gym-tracker.git

### 2. Setup Virtual Python Environment

    python -m venv venv

### 3. Activate Virtual Environment

    Windows
      .\venv\Scripts\activate
    Mac
      Look it up...

### 4. Install python dependencies

      pip install -r requirements.txt

#### If you want to view the project without kubernetes

      docker compose build
      docker compose up
      Go to this link to view the application
      https://localhost:8000

### 5. Start Kubnernetes Cluster

    minikube start --nodes 3

### 6. Apply clusters

    kubectl apply -k deploy/

### 7. Build and Load image files so that kubernetes looks for your local docker images and not from the docker repository

    docker buildx build -t django-app:latest .
    docker buildx build -t django-proxy:latest proxy/
    minikube image load django-app:latest
    minikube image load django-proxy:latest

### 8. View stats on Kebernetes dashboard

    minikube dashboard

### 9. Create admin user

    kubectl exec -it django-pod-id -c app -- python manage.py createsuperuser

## Django Commands

    python -m django startproject app
    
    python manage.py startapp gym

    python manage.py createsuperuser

    pytohn manage.py runserver
    
    python manage.py makemigrations

    python manage.py migrate

## Docker Commands - https://docker-curriculum.com/

    docker compose build

    docker compose up

    docker compose down

    docker compose run --rm app sh -c "python manage.py createsuperuser"

    docker buildx build -t django-app:latest .

    docker buildx build -t django-proxy:latest proxy/

    To delete images/volumes
  
      docker-compose down --volumes
      
      docker-compose down --rmi all --volumes

## Kubernetes Commands - https://minikube.sigs.k8s.io/docs/start/

    minikube start start --nodes 3

    minikube dashboard

    kubectl apply -k deploy/

    kubectl get deployments

    kubectl get pods

    minikube image load django-app:latest

    minikube image load django-proxy:latest

    kubectl get pvc

    kubectl get services

    kubectl service django

### Create django super user (admin)

    1. kubectl get pods -> copy name of django pod
    
    2. kubectl exec -it django-pod-id -c app -- python manage.py createsuperuser
    3. Enter superuser info
