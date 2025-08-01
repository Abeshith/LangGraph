# 🌍 LLMOps Travel Planner Agentic Application

## Overview

This project is an AI-powered Travel Planner and Expense Estimator. It leverages LLMs, agentic workflows, and real-time data tools to generate detailed, actionable travel plans for any destination. Users can interact via a Streamlit web app, receiving:
- Day-by-day itineraries
- Hotel, restaurant, and activity recommendations
- Estimated costs and budgets (with currency symbols)
- Weather and transportation info

## Project Structure

```
LLMOps/
│
├── app.py                  # Streamlit frontend for user interaction
├── main.py                 # FastAPI backend, agentic workflow server
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata and dependencies
├── .env                    # API keys and environment variables
│
├── agent/                  # Agentic workflow builder
│   └── agentic_workflow.py
│
├── config/                 # Configuration files
│   └── config.yaml
│
├── exception/              # Exception handling utilities
│   └── exception_handling.py
│
├── logger/                 # Logging utilities
│   └── logging.py
│
├── notebooks/              # Jupyter notebooks for experiments
│   └── experiments.ipynb
│
├── prompt_library/         # System and tool prompts
│   └── prompt.py
│
├── tools/                  # Modular tools for agentic workflows
│   ├── arithmetic_operation_tool.py
│   ├── currency_conversion_tool.py
│   ├── expense_calculator_tool.py
│   ├── place_search_tool.py
│   └── weather_info_tool.py
│
├── utils/                  # Utility modules
│   ├── config_loader.py
│   ├── currency_convertor.py
│   ├── expense_calculator.py
│   ├── model_loader.py
│   ├── place_info_search.py
│   ├── save_to_docs.py
│   └── weather_info.py
│
└── ... (other support files)
```

## Key Features

- **Agentic Workflow**: Modular, extensible agent built with LangGraph and LangChain
- **Real-Time Data**: Integrates with APIs for weather, places, currency, and more
- **Expense Estimation**: Calculates and formats budgets with local currency symbols
- **Custom Tools**: Arithmetic, currency conversion, place search, weather, and expense calculator tools
- **Modern UI**: Streamlit frontend for easy user interaction
- **FastAPI Backend**: Handles agentic workflow and tool orchestration

## Tools & Technologies Used

- **Python 3.11+**
- **FastAPI** (backend API server)
- **Streamlit** (frontend web app)
- **LangChain, LangGraph** (agentic workflow, LLM orchestration)
- **LangChain Community, Google, Groq, Tavily** (LLM and data providers)
- **Pydantic** (data validation)
- **Uvicorn** (ASGI server)
- **python-dotenv** (environment variable management)

## How to Run

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your `.env` file** with all required API keys (see `.env.example` or project docs)
4. **Start the backend server**
   ```bash
   python main.py
   ```
5. **Start the Streamlit frontend** (in a new terminal)
   ```bash
   streamlit run app.py
   ```
6. **Open your browser** to the Streamlit URL (usually http://localhost:8501)

## API Keys & Configuration

You will need API keys for:
- Groq, Google, OpenRouter, Tavily, OpenWeatherMap, ExchangeRate, Foursquare, etc.
Add them to your `.env` file as:
```
GROQ_API_KEY="..."
GOOGLE_API_KEY="..."
OPENROUTER_API_KEY="..."
TAVILY_API_KEY="..."
OPENWEATHERMAP_API_KEY="..."
EXCHANGE_RATE_API_KEY="..."
FOURSQUARE_API_KEY="..."
```

## Notebooks

See `notebooks/experiments.ipynb` for LLMOps experiments and prototyping.

---
**LLMOps Travel Planner Agentic Application** — AI-powered, modular, and extensible travel planning for the modern world.
