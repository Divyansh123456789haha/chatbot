
Chatbot

A full-stack chatbot for clothing brand focusing on Street Style and Classy Polo T-Shirts. This project uses a Flask backend, PostgreSQL database, and a modern HTML/CSS/JS frontend. The chatbot integrates with Groq's LLaMA API for conversational replies and Cloudinary for image hosting.

before everything main requeriments would be a api key from a LLM model which is to further prompt engineered for desired answers then a database to be connected and cloudinary for the images to be connected and post man for the final testing 
## 📁 Folder Structure

chatbot/
├── backend/
│ └── app.py
├── data.py
├── db.py
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│ ├── headphones.png
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Technologies

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Image Hosting**: Cloudinary
- **AI Model**: Groq (LLaMA 3)
- **Deployment**:
  - Frontend: Vercel
  - Backend: Localhost (Flask dev server)

---

## 🚀 Local Setup

### 1. Clone the repository

git clone https://github.com/Divyansh123456789haha/chatbot.git
cd chatbot
2. Create & activate virtual environment

python -m venv cb1
cb1\Scripts\activate  # Windows
3. Install Python packages

pip install -r requirements.txt
4. Create .env file in the root (optional if keys are hardcoded)


GROQ_API_KEY=your_groq_key
5. Run the backend

cd backend
python app.py
