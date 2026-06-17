# 📊 In-Memory Excel Chunk Splitter SaaS

A high-performance Full-Stack Django web application that processes large Excel sheets and splits them into smaller, downloadable chunks based on custom row limits (Default: 9,998 rows) — packed tightly into a single ZIP file.

## 🚀 Key Features & Architectural Decisions
- **100% In-Memory Processing:** Leverages Python's `io.BytesIO` and `pandas` to manipulate chunks entirely in RAM. **No server storage is used**, protecting user privacy and preventing server disk bloat.
- **Dynamic Chunking:** Automatically calculates and streams dynamically sliced chunks using Pandas' highly optimized vectorization (`.iloc`).
- **Modern UI:** Built a clean, responsive single-page dashboard using Tailwind CSS.
- **Enterprise Ready:** Perfect for preprocessing bulk data before uploading to restrictive legacy systems or CRMs (like Salesforce or HubSpot).

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Data Engineering:** Pandas, OpenPyXL
- **Frontend:** HTML5, Tailwind CSS
- **Archiving:** Zipfile

## 📦 Installation & Local Setup



1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AutoData_Eng/excel-splitter-django.git](https://github.com/AutoData_Eng/excel-splitter-django.git)
   cd excel-splitter-django


2. Create & activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
    pip install -r requirements.txt

4. Run the server:
    python manage.py runserver

