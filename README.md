# ✈️ Airline Management System

## 📌 Overview

A desktop-based **Airline Management System** built using **Python (PyQt5)** and **Oracle Database**.
The application simulates real-world airline operations including flight scheduling, ticket booking, payments, and database-driven logic using stored procedures and triggers.

---

## 🚀 Features

* 🛫 Flight Management
* 🎟️ Ticket Booking & Cancellation
* 👤 Passenger Management
* 💳 Payment Processing
* 📅 Live Flight Schedule (via database view)
* ⚙️ Stored Procedures, Triggers, and Views

---

## 🛠️ Tech Stack

* **Frontend:** PyQt5
* **Backend:** Python
* **Database:** Oracle DB (`oracledb`)

---

## 📂 Project Structure

```plaintext
airline_managment_system/
│
├── ui/
│   ├── main_window.py
│   ├── tabs/
│   │   ├── bookings_tab.py
│   │   ├── flights_tab.py
│   │   ├── passengers_tab.py
│   │   ├── payments_tab.py
│   │   ├── schedule_tab.py
│
├── utilies/
│   ├── helpers.py
│   ├── style.py
│
├── sql/
│   ├── 01_tables.sql
│   ├── 02_sequences.sql
│   ├── 03_procedures.sql
│   ├── 04_triggers.sql
│   ├── 05_views.sql
│   ├── 06_sample_data.sql
│
├── config/
│   └── db.py
│
├── main.py
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/krish150520/airline_managment_system.git
cd airline_managment_system
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install pyqt5 oracledb
```

---

### 4️⃣ Setup Oracle Database

Run SQL scripts in order:

```sql
@01_tables.sql
@02_sequences.sql
@03_procedures.sql
@04_triggers.sql
@05_views.sql
@06_sample_data.sql
```

---

### 5️⃣ Configure database connection

Update `config/db.py` with your Oracle credentials:

```python
user = "your_username"
password = "your_password"
dsn = "your_dsn"
```

---

### 6️⃣ Run the application

```bash
python main.py
```

---

## 📊 Database Design

* Uses relational schema with:

  * Passengers
  * Flights
  * Bookings
  * Payments

* Includes:

  * Stored Procedures (booking, cancellation, payments)
  * Trigger (prevent overbooking)
  * View (`flight_schedule`) for simplified queries

---

## 📸 Screenshots

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8f1c9883-e351-4712-8245-f92f3536de22" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c6b1989e-2a71-4a87-ad55-9ce4f9b3323c" />


---

## 🧠 Key Concepts Used

* Database normalization
* Foreign key relationships
* Triggers for business rules
* Stored procedures for logic abstraction
* UI + Database integration

---

## 👨‍💻 Author

**Krish Sharma**
GitHub: https://github.com/krish150520

---


