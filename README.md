Self-Healing Infrastructure with Prometheus, Alertmanager & Autohealer
Project Overview
This project implements a self-healing infrastructure using Prometheus, Blackbox Exporter, Alertmanager, and a custom-built Autohealer service.

The idea is simple:
Monitor Nginx availability using Prometheus + Blackbox Exporter
Trigger alerts via Alertmanager when Nginx goes down
Automatically restart the Nginx container using the Autohealer webhook
This setup ensures that if the Nginx container crashes or stops, the system will bring it back without manual intervention.

⚙️ Tech Stack
Prometheus → Monitoring & scraping metrics
Blackbox Exporter → Probing Nginx HTTP endpoint
Alertmanager → Alert routing & notifications
Flask (Autohealer Service) → Webhook receiver to restart containers
Docker & Docker Compose → Containerized setup for easy deployment

🏗️ Architecture Flow
Nginx runs in a Docker container.
Blackbox Exporter probes http://nginx:8080 for 2xx HTTP responses.
Prometheus scrapes Blackbox metrics and evaluates alert rules.
If Nginx is unreachable, Prometheus fires an alert.
Alertmanager sends the alert to the Autohealer service (webhook).
The Autohealer automatically restarts the stopped Nginx container.

How to Run
Clone the repo
git clone https://github.com/your-username/self-healing-infra.git
cd self-healing-infra
Start the setup
docker compose up -d

Access services:
prometheus → http://localhost:9090
Alertmanager → http://localhost:9093
Blackbox Exporter → http://localhost:9115
Node Exporter → http://localhost:9100
Autohealer (Flask API) → http://localhost:5000

🔎 Testing Self-Healing
Stop the Nginx container manually:
docker stop nginx

Observe the flow:
Blackbox probe → Failure
Prometheus alert fires
Alertmanager sends alert to Autohealer
Autohealer restarts Nginx container

Verify:
docker ps
You should see nginx running again automatically 

Future Improvements
Add Slack/Email notifications for alerts
Support multiple services (not just Nginx)
Implement retry & backoff mechanism for container restart
Deploy on Kubernetes for production-grade resiliency

✨ Conclusion

This project demonstrates how monitoring + alerting + automation can create a self-healing system.
Even if a critical service like Nginx fails, the infrastructure automatically recovers, reducing downtime and manual effort.
