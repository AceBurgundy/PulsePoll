# 🗳️ PulsePoll: Your Voice Matters

**PulsePoll** is a real-time, sentiment-driven voting platform where your **voice** becomes your **vote**. Rather than simply selecting a candidate, users express opinions in discussion threads. The system uses **sentiment analysis** to determine the collective attitude toward each candidate, transforming online conversation into measurable public sentiment.

Unlike traditional voting apps, PulsePoll encourages **dialogue over decision**, giving deeper insight into what people actually feel—not just who they click on.

## 🚀 Features

* 💬 **Thread-Based Candidate Discussions**
  Each candidate has a dedicated thread where users can freely express their views.

* 🧠 **Sentiment-Based Voting**
  Uses natural language processing to analyze user sentiment and infer support levels for each candidate.

* ⚡ **Real-Time Updates (Socket.IO)**
  Live broadcast of votes and sentiment changes—no page refresh required.

* 🔐 **User Authentication**
  Each user gets a unique account tied to their posts and sentiment profile.

* 📊 **Live Sentiment Dashboard**
  View real-time support scores for all candidates as users contribute.

## 👩‍💻 Prerequisites

* Python 3.8+
* (Optional) A virtual environment is recommended

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/PulsePoll
   cd PulsePoll
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

## 🗄️ Database Setup

1. Initialize the database:

   ```bash
   python create_database.py
   ```

2. Load candidate data from CSV:

   * Navigate to `Engine/candidate/` and copy the full path of `combined.csv`.
   * Open `dataset-to-database.py` and update the line:

     ```python
     dataset_path: str = "your/path/to/combined.csv"
     ```

3. Then run:

   ```bash
   python dataset-to-database.py
   ```

## ▶️ Running the App

Launch the app locally:

```bash
python app.py
```

Then open your browser to [http://localhost:8080](http://localhost:8080).

## 🌐 Tech Stack

* **Flask** – Web backend
* **Socket.IO** – Real-time messaging
* **NLTK / VADER** – Sentiment analysis engine
* **SQLite** – Lightweight database
* **HTML / CSS / JavaScript** – Frontend

## 🔮 Future Improvements

* ✍️ **User-Generated Voting Threads**
  Users will soon be able to create their own polls/threads, each containing a set of candidates—enabling community-driven discussions beyond preset elections.

* 🤖 Improved sentiment accuracy with multilingual and localized models

* 🛡️ Moderation tools for flagging and removing abusive content

* 📱 Mobile-friendly responsive design

* 🔔 Notifications for thread activity

* 🧾 Post history and user sentiment tracking

* 🗃️ Thread archiving and result exporting

> 🧪 Currently in **beta** — only fixed candidate threads are supported.

## 💡 Project Purpose

PulsePoll is an experiment in **conversational democracy**, where users influence outcomes not with a click—but with their **thoughts**. It’s built to explore how **natural language** and **collective expression** can redefine participation in digital decision-making.

## 📜 License

Licensed under the **AGPL-3.0**.
See the [LICENSE](LICENSE) file for full terms.
