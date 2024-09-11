# JobFinder API

## Overview

The **JobFinder API** is a service designed to manage job requests from management companies and find suitable vendors based on their location and compliance status. The API allows for creating jobs and vendors, as well as searching for vendors based on job requirements.

## Project Structure

The project is organized into the following main components:

- `main.py`: The entry point for the FastAPI application.
- `Dockerfile`: Configuration file for building the Docker image.
- `docker-compose.yml`: Docker Compose configuration for setting up the development environment.
- `requirements.txt`: Lists the Python dependencies for the project.
- `app/`: Contains the application code including routers, services, schemas, and repositories.
- `config/`: Contains configuration files such as authentication settings.
- `data/`: Directory for data files used by the application (e.g., vendors, jobs, categories, locations).

### Collection

A collection for tests on postman is on the Root with the name "Vendor Smart.postman_collection.json"

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose

### Building and Running the Application

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Build the Docker Image**:
    
    ```bash
    docker-compose build
3. **Start the Application**:
    ```bash
    docker-compose up

4.**Access the Application**:

- The application will be available at http://localhost:8000.
- API documentation is accessible at http://localhost:8000/docs (Swagger) and http://localhost:8000/redoc (ReDoc).

## API Endpoints
### Authentication
Basic authentication is used to secure the endpoints. Use the following credentials for authentication:

- **Username:** vs_tech_challenge
- **Password:** SuperSecurePassword123@

### Endpoints
**1. Create a Job**
- **Endpoint:** ```POST /jobs```
- **Request Body:**
    ```json
  {
  "category": "Landscaping Maintenance",
  "location": "Fayette TX"
  }
- **Response:**
    ```json
    {
      "id": 1,
      "category": "Landscaping Maintenance",
      "location": "Fayette TX"
    }
### 2. Create a Vendor

- **Endpoint:** `POST /vendors`
- **Request Body:**

    ```json
    {
      "name": "Vendor 1",
      "categories": ["Landscaping Maintenance", "Air Conditioning"],
      "location": "Fayette TX",
      "compliant": false
    }
    ```

- **Response:**

    ```json
    {
      "id": 1,
      "name": "Vendor 1",
      "compliant": false,
      "categories": ["Landscaping Maintenance", "Air Conditioning"],
      "location": "Fayette TX"
    }
    ```

### 3. Search Vendors for a Job

- **Endpoint:** `GET /vendors`
- **Query Parameters:**
  - `location`: Location of the job (e.g., "Fayette TX")
  - `category`: Service category (e.g., "Air Conditioning")

- **Response:**

    ```json
    [
      {
        "id": 1,
        "name": "Vendor 1",
        "compliant": false,
        "categories": ["Air Conditioning"],
        "location": "Fayette TX"
      },
      {
        "id": 2,
        "name": "Vendor 3",
        "compliant": true,
        "categories": ["Air Conditioning"],
        "location": "Fayette TX"
      }
    ]
    ```

### 4. Get Vendor Statistics for a Job

- **Endpoint:** `GET /vendors`
- **Query Parameters:**
  - `location`: Location of the job (e.g., "Fayette TX")
  - `category`: Service category (e.g., "Air Conditioning")

- **Response:**

    ```json
    {
      "total_vendors": 3,
      "compliant_vendors": 1,
      "non_compliant_vendors": 2
    }
    ```

## Testing and Coverage

### Preparing the environment 💻
How is nothing too complex the environment is more prepared for perform tests

Execute:
(os & Linux)

#### 1 - `virtualenv .venv` 
#### 2 - `source .venv/bin/activate` 

(Windows)

#### 1 - `python -m venv .venv` 
#### 2 - `source .venv/Scripts/activate` 

#### 3 - `pip install -r requirements.txt` 


To run the tests, use the following command:
  ```bash
    pytest
  ```

### Generating Coverage Report

To generate a coverage report, follow these steps:

1. **Install Coverage Package:** If not already installed, you need to add `coverage` to your `requirements.txt` or install it manually:

    ```bash
    pip install coverage
    ```

2. **Run Coverage Analysis:**

    ```bash
    coverage run -m pytest
    ```

3. **Generate the Coverage Report:**

    ```bash
    coverage report
    ```

4. **Generate an HTML Coverage Report:**

    ```bash
    coverage html
    ```

    The HTML report can be viewed by opening `htmlcov/index.html` in a web browser.

**Coverage Status:** The project achieves 99% test coverage.

## Documentation and Development Notes

- **Documentation:** The API is documented using FastAPI’s built-in tools. Access the interactive API documentation at `/docs` or `/redoc`.
- **Testing:** Ensure you write tests for your endpoints and services to verify functionality.
- **Improvements:** Potential improvements include adding more robust error handling, integrating with a real database, and enhancing the authentication mechanism.

## Notes

- Ensure that all the data files are properly set up in the `data/` directory before starting the application.
- The application uses file-based storage and does not currently include a database.