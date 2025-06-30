# MCP with Claude and PostgreSQL
A Model Context Protocol (MCP) implementation using Claude AI and PostgreSQL database, with a Next.js frontend and Python FastAPI backend.
## 🏗️ Architecture

Frontend: Next.js (React)
Backend: Python FastAPI (MCP Server)
Database: PostgreSQL
AI Model: Claude (Anthropic)

## 📋 Prerequisites

Node.js (v18 or higher)
Python (v3.8 or higher)
PostgreSQL
npm or yarn
pip

## 🚀 Getting Started
 ### Clone the Repository
``` git clone https://github.com/prajjwalkumarpanzade/Psql-MCP.git ```
``` cd Psql-MCP ```
### Environment Setup
Copy the example environment file and configure your settings:

Update the .env file with your actual values:

```
DB_NAME=your_database_name

DB_USER=your_username

DB_PASS=your_password

DB_HOST=localhost

DB_PORT=5432

ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

CREATE DATABASE your_database_name;

### Backend Setup (Python FastAPI)

Navigate to the backend directory and install dependencies:

```
cd service

pip install -r requirements.txt
```
### Run the FastAPI server:
```
uvicorn main:app --reload 
```
The API will be available at http://localhost:8000
 
### Frontend Setup (Next.js)
Navigate to the frontend directory and install dependencies:

```
cd app

npm install
   or
yarn install
```
Run the development server:
```
npm run dev 
  or
yarn dev
```
The application will be available at http://localhost:3000
