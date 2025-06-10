### ⚙️ Repository: `backend`

#### 📦 Description
FastAPI backend app in Python.

#### 🛠️ Run with Docker
```bash
git clone https://github.com/nirmalskandan/backend.git
cd backend
docker build -t backend-app .
docker run -p 8000:8000 backend-app
```

#### 🚀 Run Locally (Without Docker)
```bash
git clone https://github.com/nirmalskandan/backend.git
cd backend
## 🛠️ Backend Setup (FastAPI + MongoDB)

### ✅ Set Up Python Virtual Environment

```bash
cd backend
python -m venv .venv
```

#### 🔁 Activate `.venv` Based on Your Shell:

* **macOS/Linux (bash/zsh):**

  ```bash
  source .venv/bin/activate
  ```
* **Windows CMD:**

  ```cmd
  .venv\Scripts\activate.bat
  ```
* **Windows PowerShell (Recommended):**

  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  .venv\Scripts\Activate.ps1
  ```

### ✅ Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ Update MongoDB Connection Logic

Ensure your `backend/app/main.py` includes:

```python
from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/mydatabase")
client = MongoClient(MONGO_URL)
db = client.get_database()
```

### ✅ Set Environment Variable for Local Use

Run this **after activating the virtual environment**:

* **macOS/Linux:**

  ```bash
  export MONGO_URL="mongodb://localhost:27017/mydatabase"
  ```
* **Windows PowerShell:**

  ```powershell
  $env:MONGO_URL = "mongodb://localhost:27017/mydatabase"
  ```

### ✅ Start FastAPI Backend Locally

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/mongo-test](http://localhost:8000/mongo-test) to test MongoDB connection.

> Ensure CORS is enabled in FastAPI if frontend is on a different port.

### ✅ Troubleshooting

If `uvicorn` is not recognized:

```bash
pip install uvicorn
```

If `pymongo` is missing:

```bash
pip install pymongo
```


---