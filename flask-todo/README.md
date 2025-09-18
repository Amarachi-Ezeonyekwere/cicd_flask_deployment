# 📝 Flask To-Do App (Containerized with CI/CD)

## 📌 Project Overview
This project is a **simple Python Flask-based To-Do List application**, containerized using **Docker** and automated through a **CI/CD pipeline**.  
The goal is to showcase practical **DevOps and Cloud Computing skills** while solving a real-world business need: **managing tasks efficiently and reliably**.

---

## 💡 Business Problem
Managing tasks is a common challenge for both individuals and teams.  
The **Flask To-Do App** solves this by:
- Providing a lightweight, web-based task management solution.  
- Running in a **containerized environment** for easy deployment.  
- Ensuring consistent builds and deployments through **CI/CD automation**.  
- Storing tasks in a persistent **SQLite database**, so no data is lost between runs.  

This mimics how modern organizations manage microservices: reliable, reproducible, and scalable.

---

## ⚙️ Tech Stack
- **Python** (Flask framework) – backend web application.  
- **SQLite** – lightweight, persistent database for storing tasks.  
- **Docker** – containerization for portability and reproducibility.  
- **Docker Hub** – image repository for storing and sharing builds.  
- **CI/CD Pipeline** – automates build and push steps (e.g., GitHub Actions or similar).  

---

## ✅ What Has Been Done
- Built a **Flask web app** for a simple to-do list.  
- Containerized the app with a **Dockerfile**.  
- Configured **docker-compose.yml** for local development.  
- Pushed Docker images automatically to **Docker Hub** using CI/CD.  
- Verified **database persistence** (tasks remain available after restarts).  

---

## 🔄 Ongoing & Future Iterations
This project is continuously evolving to demonstrate advanced DevOps practices:

1. **Security Enhancements**
   - Add **SAST (Static Application Security Testing)** to scan for code vulnerabilities.  
   - Add Trivy **dependency vulnerability checks** before integration and deployment.  

2. **Kubernetes Deployment**
   - Extend deployment to a **Kubernetes cluster** for scalability and reliability.  
   - Configure **Helm charts** or Kubernetes manifests for automated rollout.  

3. **Monitoring & Observability**
   - Integrate monitoring tools (e.g., Prometheus, Grafana).  
   - Add centralized logging with ELK stack (Elasticsearch, Logstash, Kibana).  

4. **Cloud Deployment**
   - Push the application to a cloud provider (AWS) with IaC tools like **Terraform**.  

---

## 🚀 How to Run Locally
Clone the repository:
```bash
git clone https://github.com/your-username/flask-todo.git
cd flask-todo
````

Build and run with Docker:

```bash
docker-compose up --build
```

Access the app at:
👉 [http://localhost:5000](http://localhost:5000)

---

## 🤝 Contributing

* Fork the repository.
* Create a feature branch (`git checkout -b feature-name`).
* Commit your changes and push.
* Open a Pull Request.

Contributions, suggestions, and improvements are welcome!

---

## 📈 Why This Project Matters

This repository is part of my **DevOps & Cloud Engineering journey**.
It highlights my ability to:

* Build and containerize applications.
* Automate deployments with CI/CD.
* Implement ongoing improvements in **security, scalability, and observability**.


