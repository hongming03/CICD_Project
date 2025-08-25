CICD Project from Scratch
1. Develop the app - include /health enpoint for docker compose health checks
2. Use environment variables via .env
3. Develop unit test cases, create Mock object for test cases that needs to use external services. This is to simulate real services so that unit test can fail-fast and not have to spin up actual services in github actions
5. Develop Integration tests with services on your local machine or with docker compose (exec integration test in your web service)
6. Containerized your application using Dockerfile and make sure it works
7. Use docker-compose to spin up the services and make sure to update environment variables in .env to match service names. Important to include health checks (for github actions)
8. Test if integration test works in docker compose
9. Push Code to Github (except .env) and set up Repository Variables/Secrets. Note: After commiting empty key .env file. Add .env to .gitignore and git rm --cached .env to stop pushing it to git.
10. Modify .yml files to use github Repository Variables/Secrets
11. Create CICD Pipeline, ensure that the CICD works
12. 

Blockers that was ran into during project:
1. Volume not deleted causing the db table to not create in local environment
2. Postgres database did not create in time leading to failed integration test - requires healthcheck



