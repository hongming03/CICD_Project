CICD Project from Scratch
----- Unit Tests -----
1. Develop the app - include /health enpoint for docker compose health checks
2. Use environment variables via .env
3. Develop unit test cases, create Mock object for test cases that needs to use external services. This is to simulate real services so that unit test can fail-fast and not have to spin up actual services in github actions

----- Continuos Integration -----
5. Develop Integration tests with services on your local machine or with docker compose (exec integration test in your web service container, docker exec)
6. Containerized your application using Dockerfile and make sure it works
7. Use docker-compose to spin up the services and make sure to update environment variables in .env to match service names. Important to include health checks (for github actions)
8. Test if integration test works in docker compose
9. Push Code to Github (except .env) and set up Repository Variables/Secrets. Note: After commiting empty key .env file. Add .env to .gitignore and git rm --cached .env to stop pushing it to git.
10. Modify .yml files to use github Repository Variables/Secrets
11. Create CICD Pipeline, ensure that the CICD works until integration test(docker compose)

----- Deployment -----
12. Push your web image to docker hub
13. Create Self-hosted runner for deployment job ( run.cmd to run self hosted runner)
14. Configure deployment yaml for kubernetes
15. Configure Deployment in CICD (github actions)

Blockers that was ran into during project:
1. Postgres database did not create in time leading to failed integration test - requires healthcheck


minikube start
run your github actions runner

1. Use environment variables for deployment.yml
2. Do slack noti
3. Film video of this proj

need to store 

db host name
db user
db password


