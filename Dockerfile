# 1️⃣ Base image
FROM python:3.11-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy requirements first (better caching)
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy entire project
COPY . .

# 6️⃣ Expose port
EXPOSE 8000

# 7️⃣ Run FastAPI using uvicorn
CMD ["uvicorn", "src.__init__:app", "--host", "0.0.0.0", "--port", "8080"]