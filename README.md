# FastAPI Dockerized Application

This repository contains a FastAPI application Dockerized for easy deployment and management. Follow the steps below to set it up:

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd your-repo
    ```

3. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

4. **Activate the Virtual Environment:**

    ```bash
    source venv/bin/activate
    ```

5. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Build Docker Image:**

    ```bash
    docker-compose build
    ```

7. **Start Docker Containers:**

    ```bash
    docker-compose up -d
    ```

    This command will start the Docker containers in detached mode.

8. **Access the FastAPI Application:**

    Once the containers are up and running, you can access the FastAPI application at [http://localhost:8000](http://localhost:8000).

9. **Access PgAdmin:**

    You can also access PgAdmin on your browser at [http://localhost:5050](http://localhost:5050). Use the following credentials to log in:

    - **Username:** admin@gmail.com
    - **Password:** admin

    Once you are logged in to PgAdmin, follow these steps to register the server:

    1. Click on the "Add New Server" icon or go to the "Servers" menu and select "Create" > "Server".
    2. In the "General" tab, enter a name for the server (e.g., "FastAPI PostgreSQL Server").
    3. In the "Connection" tab:
       - **Host name/address:** Enter `fastapi-db`, which is the container name defined in the `docker-compose.yml` file.
       - **Port:** Keep the default port `5432`.
       - **Username:** Enter `postgres`.
       - **Password:** Enter `admin`, as specified in the `.env` file.
    4. Click "Save" to register the server.

    Now you should be able to access and manage the PostgreSQL server from PgAdmin.


## Additional Information

- Modify the `docker-compose.yml` file and `.env` file as needed for your specific environment.
- Make sure ports `8000`, `5050`, and any other necessary ports are available and not being used by other services on your machine.
- Remember to deactivate the virtual environment once you're done working with the application:

    ```bash
    deactivate
    ```

For more information on FastAPI, Docker, and PgAdmin, refer to their respective documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [PgAdmin Documentation](https://www.pgadmin.org/docs/)
