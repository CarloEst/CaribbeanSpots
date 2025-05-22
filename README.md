
# 🌴 Caribbean Spots — Restaurant Discovery Web App

**Caribbean Spots** is a Flask-based web application that helps users discover and explore Caribbean restaurants around them. Whether you're looking for jerk chicken, mofongo, or curry goat, this app brings the taste of the Caribbean closer to you with a clean interface and smooth user experience.

---

## 🚀 Features

- 🔍 **Search Functionality**: Find restaurants by name or country of origin.
- 📋 **Add New Restaurants**: Input and store new Caribbean restaurants with all essential info.
- ✏️ **Edit Restaurant Details**: Modify restaurant listings directly from the UI.
- ⭐ **Ratings, Popular Dishes, and Price Ranges**: View quick summaries to help decide.
- 🌐 **Online Delivery Options**: Know which platforms (Grubhub, DoorDash, etc.) are supported.
- 🧠 **View Similar Restaurants**: Get recommendations based on current selections.
- 🎨 **Responsive UI**: Styled using custom CSS and Bootstrap 4 for mobile and desktop.

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS (custom + Bootstrap), JavaScript

````

## 📂 File Structure


.
├── server.py              # Flask app routing logic
├── templates/             # HTML pages (Jinja templates)
│   ├── homepage.html
│   ├── add.html
│   ├── edit.html
│   ├── view.html
│   ├── search.html
│   └── layout.html
├── static/
│   ├── style.css          # Custom theme and layout styling
│   └── style.js           # Client-side interactivity (e.g., form checks)
```

---

## 🧪 Running the App Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/caribbean-spots.git
   cd caribbean-spots
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the server:
   ```bash
   python server.py
   ```

5. Visit [http://localhost:5001](http://localhost:5001) in your browser.

---


