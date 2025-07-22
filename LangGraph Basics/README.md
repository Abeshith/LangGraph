# LangGraph Basics

Learn the fundamental concepts of LangGraph through hands-on examples. This folder contains essential building blocks for understanding how to create stateful, multi-step applications with Large Language Models.

## 📚 What You'll Learn

- **State Management**: How LangGraph maintains information across conversation turns
- **Graph Construction**: Building workflows as directed graphs with nodes and edges
- **Basic Agents**: Creating simple AI agents that can reason and act
- **Human-in-the-Loop**: Incorporating human feedback into agent workflows
- **Streaming**: Real-time response streaming from agents

## 📁 Files Overview

### 1. `basic_langgraph.ipynb`
**Core LangGraph Concepts**
- State definition and management
- Creating nodes (functions that agents execute)
- Building a simple graph structure
- Adding edges and conditional logic
- Compiling and running your first agent

**Key Concepts Covered:**
- `StateGraph` creation
- Node definition with `@tool` decorator
- State typing with `TypedDict`
- Graph compilation and execution

### 2. `human_in_loop.ipynb`
**Interactive Agent Workflows**
- Adding human approval steps
- Conditional execution based on user input
- Interrupt and resume functionality
- Building approval workflows

**Use Cases:**
- Content moderation before publishing
- Financial transaction approvals
- Critical decision checkpoints
- User preference collection

### 3. `streaming.ipynb`
**Real-time Agent Responses**
- Streaming responses from agents
- Real-time progress updates
- Handling partial results
- Stream processing and display

**Benefits:**
- Better user experience with immediate feedback
- Monitoring long-running processes
- Real-time debugging and observation

## 🚀 Quick Start Workflow

### Basic Agent Creation
The basic pattern involves defining your state structure, creating nodes (agent functions), building the graph with proper edges, and compiling for execution.

### Human-in-the-Loop Pattern
Add interrupt nodes for human input and implement conditional edges that route to human approval when needed, allowing for interactive workflows.

## 🎯 Learning Exercises

### Exercise 1: Simple Chatbot
Create a basic conversational agent that:
1. Maintains conversation history
2. Responds to user queries
3. Tracks conversation state

### Exercise 2: Approval Workflow
Build an agent that:
1. Generates content suggestions
2. Asks for human approval
3. Revises based on feedback
4. Finalizes approved content

### Exercise 3: Multi-Step Reasoning
Create an agent that:
1. Breaks down complex problems
2. Solves each step incrementally
3. Streams progress updates
4. Provides final comprehensive answer

## 🔧 Common Patterns

### State Definition
Define state using TypedDict with proper type annotations, including message handling and tracking current task or user preferences.

### Conditional Logic
Implement routing logic functions that examine state and return appropriate next node names based on conditions like approval requirements or completion status.

## 🐛 Common Issues & Solutions

### Issue: State Not Updating
**Problem**: Changes to state don't persist between nodes
**Solution**: Always return state updates from node functions

### Issue: Graph Execution Hangs
**Problem**: Missing edges or circular references
**Solution**: Ensure all paths lead to END node

### Issue: Type Errors
**Problem**: State type mismatches
**Solution**: Use proper TypedDict definitions and type hints

## 📖 Next Steps

After mastering these basics, explore:
- **[LangGraph Tools](../LangGraph%20Tools/)** - Add external capabilities
- **[LangGraph Multi Agents](../LangGraph%20Multi%20Agents/)** - Coordinate multiple agents
- **[LangGraph RAG Agents](../LangGraph%20RAG%20Agents/)** - Build knowledge-based systems


Remember: LangGraph is about creating **stateful workflows**. Think of each node as a step in a process, and the state as the information that flows between steps!
