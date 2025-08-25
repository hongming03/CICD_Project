CICD Project from Scratch
1. Develop the app 
2. Use environment variables via .env
3. Develop unit test cases, create Mock object for test cases that needs to use exxternal services. This is to simulate real services so that unit test can fail-fast and not have to spin up actual services
4. Containerized your application using Dockerfile and make sure it works
5. Use docker-compose to spin up the services and make sure to update environment variables in .env to service names
6. Push Code to Github (except .env) and set up Repository Variables/Secrets 
7. Modify .yml files to use github Repository Variables/Secrets
8. Create CICD Pipeline, ensure that the CICD works


