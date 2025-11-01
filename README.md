# 💳 Credit Card Statement Parser

This project is a Python-based PDF parser that extracts 5 key data points from credit card statements across 5 different issuers.

## ✨ Stand-Out Features

This project was designed to be robust, scalable, and professional—not just a single script.

- **Modular Parser Factory:** The system uses an Abstract Base Class (`BaseParser`) to create a scalable "factory" pattern. This makes it easy to add new banks (like `ChaseParser`, `AmexParser`, etc.) without breaking any existing code.
- **Interactive Web UI:** The parser is wrapped in a user-friendly Streamlit web application for live demonstration.
- **Containerized Delivery:** The entire application is containerized with Docker, allowing for a one-click, "it just works" evaluation.

## 🚀 How to Run (Docker)

This is the recommended way to run the project.

1.  **Build the Docker image:**

    ```bash
    docker build -t card-parser .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 8501:8501 card-parser
    ```

3.  **Open the app in your browser:**
    [http://localhost:8501](http://localhost:8501)

---

### How to Run (Locally)

1.  Create a virtual environment: `python -m venv venv`
2.  Activate it: `.\venv\Scripts\activate.ps1`
3.  Install dependencies: `pip install -r requirements.txt`
4.  Run the app: `streamlit run app.py`
