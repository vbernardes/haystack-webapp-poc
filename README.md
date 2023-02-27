# Document Retrieval / QA Proof of Concept (PoC)

This project contains a proof of concept for a Haystack-based application that implements document retrieval and question answering. Haystack is an open-source library that provides functionalities for extracting information from large text corpora.

## Running

To run the project, follow these steps:

1. Install Docker and Docker Compose.
2. Clone this repository to your local machine.
3. Navigate to the root directory of the repository in your terminal.
4. Run `docker-compose up -d` to start the containers.
5. Open your web browser and go to `http://localhost:8501` to access the web application.

## Features
The current version of the application provides three main features, which are implemented in separate sections:

### Load Data
This section is not implemented yet.

### Document Retrieval
This section allows you to search for documents containing a specific keyword or phrase. To use it, type your query in the text input box and press Enter. The application will send a request to a Haystack server with the query and retrieve a list of relevant documents.

### Question Answering
This section allows you to ask a question and receive an answer from the Haystack server. To use it, type your question in the text input box and press Enter. The application will send a request to a Haystack server with the question and retrieve the most relevant answers. The answers will be displayed along with their score and context.

## Improvements
- [ ] Rewrite the REST API server, so we don't need to run one Haystack container per pipeline (e.g., one for document retrieval and another for question answering).
- [ ] Deploy to cloud provider.