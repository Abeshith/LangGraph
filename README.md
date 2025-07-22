# LangGraph Learning Repository

Welcome to the LangGraph Learning Repository! This comprehensive collection contains hands-on examples, tutorials, and practical implementations of LangGraph - a powerful library for building stateful, multi-actor applications with LLMs.

## 🚀 What is LangGraph?

LangGraph is a library for building stateful, multi-actor applications with Large Language Models (LLMs). It extends LangChain with the ability to coordinate multiple actors in a structured graph format, enabling complex workflows, agent interactions, and stateful conversations.

## 📁 Repository Structure

| Folder | Description | Key Features |
|--------|-------------|--------------|
| **[LangGraph Basics](./LangGraph%20Basics/)** | Foundation concepts and basic implementations | Core concepts, state management, simple graphs |
| **[LangGraph Debugging](./LangGraph%20Debugging/)** | Debugging tools and techniques | LangSmith integration, debugging workflows |
| **[LangGraph Multi Agents](./LangGraph%20Multi%20Agents/)** | Multi-agent systems and coordination | Agent communication, supervised workflows |
| **[LangGraph RAG Agents](./LangGraph%20RAG%20Agents/)** | Retrieval-Augmented Generation implementations | Document retrieval, knowledge-based agents |
| **[LangGraph SQL Agent](./LangGraph%20SQL%20Agent/)** | Database interaction and SQL query agents | Database connectivity, SQL generation |
| **[LangGraph Tools](./LangGraph%20Tools/)** | Custom tools and integrations | Tool creation, external API integration |
| **[Curie Radiation Documents](./Curie_Radiation_Documents/)** | Sample documents for RAG examples | Historical documents, text corpus |

## 🛠️ Quick Start

### Prerequisites
- Python 3.11+
- Virtual environment (recommended)
- API keys for LLM services (OpenAI, Groq, etc.)

### Setup
1. **Clone or navigate to this repository**
2. **Activate your virtual environment** (langgraph-handson folder contains the virtual environment)
   ```bash
   # Windows
   .\langgraph-handson\Scripts\Activate.ps1
   
   # Or activate.bat for Command Prompt
   .\langgraph-handson\Scripts\activate.bat
   ```
3. **Set up environment variables**
   - Copy `.env.example` to `.env` (if available)
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_key
     GROQ_API_KEY=your_groq_key
     LANGSMITH_API_KEY=your_langsmith_key
     ```

### Learning Path

#### 🌱 Beginner (Start Here)
1. **[LangGraph Basics](./LangGraph%20Basics/)** - Learn core concepts
2. **[LangGraph Tools](./LangGraph%20Tools/)** - Understand tool integration

#### 🌿 Intermediate
3. **[LangGraph Multi Agents](./LangGraph%20Multi%20Agents/)** - Multi-agent coordination
4. **[LangGraph RAG Agents](./LangGraph%20RAG%20Agents/)** - Document-based reasoning

#### 🌳 Advanced
5. **[LangGraph SQL Agent](./LangGraph%20SQL%20Agent/)** - Database interactions
6. **[LangGraph Debugging](./LangGraph%20Debugging/)** - Production debugging

## 🎯 Key Learning Outcomes

By working through this repository, you'll learn:

- **State Management**: How to maintain conversation and application state
- **Graph Construction**: Building complex workflows as directed graphs
- **Agent Coordination**: Managing multiple AI agents working together
- **Tool Integration**: Creating and using custom tools with agents
- **RAG Implementation**: Building retrieval-augmented generation systems
- **Database Integration**: Creating SQL-capable AI agents
- **Debugging & Monitoring**: Using LangSmith for debugging and observability

## 🔄 Common Workflows

### Basic Agent Workflow
1. Define state structure
2. Create nodes (functions)
3. Build the graph
4. Add edges and conditions
5. Compile and run

### Multi-Agent Workflow
1. Define shared state
2. Create specialized agents
3. Set up communication patterns
4. Implement supervision logic
5. Handle conflicts and coordination

### RAG Workflow
1. Prepare document corpus
2. Set up vector store
3. Create retrieval tools
4. Build reasoning agent
5. Implement answer synthesis

## 🤝 Contributing

This is a learning repository. Feel free to:
- Add your own examples
- Improve existing notebooks
- Share interesting use cases
- Report issues or suggestions

## 📚 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangSmith for Debugging](https://smith.langchain.com/)

## ⚠️ Note

This repository is for educational purposes. Make sure to:
- Keep your API keys secure
- Review costs before running experiments
- Test in development before production use

Happy learning! 🎉
