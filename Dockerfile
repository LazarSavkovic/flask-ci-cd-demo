# 1) Base image with Python
FROM python:3.12-slim

# 2) Set working directory inside the container
WORKDIR /app

# 3) Install system dependencies (often useful for real projects)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# 4) Copy dependency list first (better caching)
COPY requirements.txt .

# 5) Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy the rest of the project
COPY . .

# 7) Expose the port our Flask app runs on
EXPOSE 5000

# 8) Avoid debug mode in container
ENV FLASK_ENV=production

# 9) Command to run the app
CMD ["python", "app.py"]
