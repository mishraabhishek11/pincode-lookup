# 📮 Pincode Lookup – FastAPI Service

A lightweight **FastAPI application** that resolves Indian **PIN codes** to their **city, district and state**, with single and bulk lookup endpoints.

This project demonstrates **REST API design**, request validation with Pydantic, and custom error handling.

---

## 🚀 Features

### 🔍 Single Lookup

- Look up a 6-digit PIN code via `GET /pincode/{code}`
- Returns pincode, city, district and state

### 📦 Bulk Lookup

- Look up up to **20** PIN codes in one `POST /pincode/bulk` request
- Response reports counts of found / not found codes, plus the matched results and the missing codes

### ✅ Validation & Error Handling

- PIN codes must be exactly 6 digits
- Custom JSON error responses for invalid and unknown PIN codes
- Auto-generated interactive docs (Swagger UI / ReDoc)

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Server:** Uvicorn
- **Data Store:** In-memory dictionary (`data.py`)

---

## 📂 Project Structure

```
pincode-lookup/
├─ README.md
├─ requirements.txt
├─ main.py          # FastAPI app and route definitions
├─ models.py        # Pydantic request/response models and validators
├─ data.py          # In-memory PIN code dataset
└─ exceptions.py    # Custom exceptions and their HTTP handlers
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mishraabhishek11/pincode-lookup.git
```

### 2️⃣ Navigate to the project folder

```bash
cd pincode-lookup
```

### 3️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Start the server

```bash
uvicorn main:app --reload
```

### 6️⃣ Open in browser

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🧑‍💻 Usage

### Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Health/welcome message |
| GET | `/pincode/{code}` | Look up a single PIN code |
| POST | `/pincode/bulk` | Look up multiple PIN codes (1–20) |

### Single lookup

```bash
curl http://localhost:8000/pincode/110001
```

```json
{
  "pincode": "110001",
  "city": "New Delhi",
  "state": "Delhi",
  "district": "Central Delhi"
}
```

### Bulk lookup

```bash
curl -X POST http://localhost:8000/pincode/bulk \
  -H "Content-Type: application/json" \
  -d '{"pincodes": ["110001", "400001", "999999"]}'
```

```json
{
  "status": "success",
  "found": 2,
  "not_found": 1,
  "results": [
    { "pincode": "110001", "city": "New Delhi", "state": "Delhi", "district": "Central Delhi" },
    { "pincode": "400001", "city": "Mumbai", "state": "Maharashtra", "district": "Mumbai City" }
  ],
  "missing": ["999999"]
}
```

---

## ⚠️ Error Responses

| Status | Error | When |
|---|---|---|
| 400 | `invalid_pincode` | Single lookup code is not exactly 6 digits |
| 404 | `pincode_not_found` | Code is valid but not in the dataset |
| 422 | FastAPI validation error | Bulk request is empty, has more than 20 codes, or contains a malformed code |

Example (`GET /pincode/abc`):

```json
{
  "error": "invalid_pincode",
  "message": "Pincode 'abc' is invalid: pin code must be 6 digit ",
  "pincode": "abc"
}
```

---

## 🗂️ Available Data

The dataset currently covers major cities only: Delhi (110001), Mumbai (400001), Bangalore (560001), Chennai (600001), Kolkata (700001), Hyderabad (500001), Pune (411001), Ahmedabad (380001), Jaipur (302001), Lucknow (226001), Kochi (682001), Nagpur (440001), Patna (800001), Chandigarh (160001) and Noida (201301).

---

## 🎯 Learning Objectives

- Build REST endpoints with FastAPI
- Validate input using Pydantic models and validators
- Implement custom exceptions and handlers
- Design consistent request/response shapes

---

## 🔮 Future Enhancements

- Replace the in-memory dictionary with a database or full India Post dataset
- Reverse lookup (city/district → PIN codes)
- Unit and integration tests
- Docker support
- Caching and rate limiting

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch  
   `git checkout -b feat/your-feature`
3. Commit your changes  
   `git commit -m "feat(scope): add your message"`
4. Push to the branch  
   `git push origin feat/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Abhishek Mishra  
GitHub: https://github.com/mishraabhishek11

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
