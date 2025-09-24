##  Project Overview  

This project is a **Python Flask-based To-Do List application** built to demonstrate **end-to-end DevOps, DevSecOps and Cloud Engineering practices**.  

##  Key highlights:  
- **Containerized with Docker** for easy portability  
- **Automated CI/CD with GitHub Actions**, including:  
  - Build & push of Docker images to Docker Hub and Amazon EKS  
  - Security checks (Trivy, Hadolint, pip-audit, Gitleaks)  
  - Automated testing & validation before deployment  
- **Infrastructure as Code with Terraform** for AWS resources (EKS, S3, CloudWatch)  
- **Kubernetes (EKS)** for scalable, resilient orchestration  
- **Future enhancements**: Helm charts, GitOps with ArgoCD, advanced monitoring (Prometheus, Grafana)  

---

##  Business Problem  

Task management is a **common business requirement**, but organizations need more than just a to-do list.  
They require applications that are:  
- **Secure** → free from vulnerabilities and secrets exposure  
- **Reliable** → tested, monitored, and resilient to failure  
- **Scalable** → able to handle growth without performance issues  

This project addresses task management while also demonstrating how to build, test, secure, and deploy applications in a **production-ready DevSecOps pipeline**.  

---

##  Why This Project Matters  

This repository simulates a **real-world DevSecOps workflow** from end to end:  
- **Code development** → write features in Python (Flask)  
- **Security enforcement** → integrate automated scans and dependency audits  
- **CI/CD delivery** → build, test, and push with GitHub Actions  
- **Cloud-native deployment** → orchestrate containers on AWS EKS with Terraform  

It goes beyond solving task management — it shows how modern engineering teams can:  
- **Reduce risks** by embedding security early  
- **Ensure quality** through automated testing and pipelines  
- **Deliver faster** with scalable, repeatable infrastructure  

The goal is not just to build an app, but to showcase **complete DevSecOps and Cloud Engineering skills** that are directly applicable to enterprise scenarios.