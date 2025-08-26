## CI/CD Project from Scratch

### Unit Tests
1. Develop the app – include a `/health` endpoint for Docker Compose health checks
2. Use environment variables via GitHub Actions secrets (no `.env` file)
3. Develop unit test cases, create mock objects for tests requiring external services to simulate real services for fail-fast testing

### Continuous Integration
4. Develop integration tests with services on your local machine or using Docker Compose (`docker exec` into web container)
5. Containerize the application using Dockerfile and ensure it works
6. Use Docker Compose to spin up services and include health checks
7. Test if integration tests work with Docker Compose
8. Push code to GitHub (excluding `.env`) and set up repository secrets
9. Modify GitHub Actions workflow `.yml` files to use repository secrets
10. Ensure CI pipeline runs successfully until integration tests

### Deployment
11. Push web image to Docker Hub
12. Set up GitHub Actions self-hosted runner (`run.cmd`)
13. Configure Kubernetes deployment YAML
14. Configure deployment job in GitHub Actions using the self-hosted runner

## Blockers
- PostgreSQL database did not start in time, causing failed integration tests – resolved using health checks

## Showcase / Running the Project
1. Start Minikube (`minikube start --driver=docker`)
2. Start GitHub Actions self-hosted runner (`run.cmd`)
3. Enable the workflow and actions on Github
4. Push code to GitHub
5. Port forward to the web service (`minikube service web --url`) – not needed if Minikube runs on Hyper-V or a VM

## Clean Up
1. Delete Kubernetes deployment (`kubectl delete -f ./k8s/`)
2. Stop Minikube (`minikube stop`)