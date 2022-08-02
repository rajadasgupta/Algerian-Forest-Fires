# Algerian-Forest-Fires
predict the fire area of forest fires using meteorological and other data

Steps to be followed:

1. Create a GIT reporsitory and add readme, Licesne and gitignore file
2. Create the environment for the project
    conda create -p venv python==3.7 -y 
3. Activate conda environment (from cmd prompt)
    conda activate venv\
4. Tested the Exception and loggin code
5. Added .github\workflow file for CI/CD pipleline
6. create the app in Heroku and generate the API key
7. Add the secrets in GITHUB with the heroku secrets
8. Add the dockerfile before deplying the code in heroku
9. Build the docker image: <forest-ml-project> is the docker image name
    docker build -t forest-ml-project:latest .
10. to list the docker images and check the image is built correctly
    docker images (#get the docker image ID to run the docker image)
11. to run docker image
    docker run -p 5000:5000 -e PORT=5000 <docker imageID>
12. To check running docker images
    docker ps (#get the container ID of the running image)
13. To stop running container
    docker stop <container_ID>    
14. 