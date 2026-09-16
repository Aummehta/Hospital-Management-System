# Doctor Appointment Management System

A comprehensive doctor appointment management application built with FastAPI (Python) and React for managing patients, doctors, appointments, and medical records.

## Features

- **Patient Management** - Register and manage patient records
- **Doctor Management** - Handle doctor profiles and schedules
- **Appointment Booking** - Schedule and manage appointments
- **Medical Records** - Maintain patient medical history and prescriptions
- **Admin Dashboard** - Administrative controls and reporting
- **Multi-role Access** - Different interfaces for admins, doctors, and patients

## Tech Stack

- **Backend**: Python 3, FastAPI, Beanie (ODM)
- **Frontend**: React.js
- **Database**: MongoDB

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aummehta/Hospital-Management-System.git
   cd Hospital-Appointment-system
   ```

2. **Backend Setup**
   ```bash
   cd Backend
   # It is recommended to create a virtual environment first
   python -m venv venv
   # Activate it (Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate)
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the FastAPI server
   python main.py
   ```

3. **Frontend Setup (in a new terminal)**
   ```bash
   cd Frontend
   npm install
   
   # Start the React development server
   npm start
   ```

## Usage

- **Admin**: Manage doctors, patients, and appointments
- **Doctor**: View schedules, patient records, and prescriptions
- **Patient**: Book appointments and view medical records

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
