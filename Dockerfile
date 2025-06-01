# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit (8501) and FastAPI (8000)
EXPOSE 8000
EXPOSE 8501

# Run the app
CMD ["python", "app.py"]
