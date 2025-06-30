MCP with Claude and PostgreSQL
A Model Context Protocol (MCP) implementation using Claude AI and PostgreSQL database, with a Next.js frontend and Python FastAPI backend.
🏗️ Architecture

Frontend: Next.js (React)
Backend: Python FastAPI (MCP Server)
Database: PostgreSQL
AI Model: Claude (Anthropic)

📋 Prerequisites

Node.js (v18 or higher)
Python (v3.8 or higher)
PostgreSQL
npm or yarn
pip

🚀 Getting Started
1. Clone the Repository
bashgit clone <your-repo-url>
cd <your-project-name>
2. Environment Setup
Copy the example environment file and configure your settings:
bashcp example.env .env
Update the .env file with your actual values:
envDB_NAME=your_database_name
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
ANTHROPIC_API_KEY=your_anthropic_api_key_here
3. Database Setup
Create a PostgreSQL database and ensure it's running:
bash# Create database (if not exists)
createdb your_database_name

# Or using psql
psql -U postgres
CREATE DATABASE your_database_name;
4. Backend Setup (Python FastAPI)
Navigate to the backend directory and install dependencies:
bashcd backend  # or wherever your Python code is located
pip install -r requirements.txt
Run the FastAPI server:
bashuvicorn main:app --reload --host 0.0.0.0 --port 8000
The API will be available at http://localhost:8000
5. Frontend Setup (Next.js)
Navigate to the frontend directory and install dependencies:
bashcd frontend  # or wherever your Next.js code is located
npm install
# or
yarn install
Run the development server:
bashnpm run dev
# or
yarn dev
The application will be available at http://localhost:3000
