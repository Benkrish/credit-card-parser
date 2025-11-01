# 1. Start with a lightweight Python image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the "parts list" in first
COPY requirements.txt .

# 4. Install all the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your project code (app.py, parser/, etc.) into the container
COPY . .

# 6. Tell Docker your app runs on this port
EXPOSE 8501

# 7. The command to start your app when the container runs
CMD ["streamlit", "run", "app.py"]