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
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Visit: http://localhost:8000/docs

---