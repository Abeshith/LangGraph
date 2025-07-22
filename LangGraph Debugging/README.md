# LangGraph Debugging

Master the art of debugging and monitoring LangGraph applications using LangSmith and advanced debugging techniques. This folder provides tools and examples for production-ready agent development.

## 🔍 What You'll Learn

- **LangSmith Integration**: Advanced tracing and monitoring
- **Debug Workflows**: Step-by-step debugging techniques
- **Performance Monitoring**: Tracking agent performance and costs
- **Error Handling**: Robust error management strategies
- **Production Debugging**: Real-world debugging scenarios

## 📁 Files Overview

### 1. `agent.py`
**Production Agent Implementation**
- Complete agent setup with error handling
- LangSmith tracing integration
- Environment configuration
- Tool integration with debugging capabilities

**Key Features:**
- Structured logging and tracing
- Error boundaries and fallback mechanisms
- Performance monitoring hooks
- State inspection utilities

### 2. `debug.ipynb`
**Interactive Debugging Notebook**
- Step-by-step debugging workflows
- State inspection techniques
- LangSmith trace analysis
- Performance profiling examples

**Debugging Techniques:**
- Breakpoint insertion in agent flows
- State visualization and inspection
- Error reproduction and analysis
- Performance bottleneck identification

### 3. `langgraph.json`
**LangGraph Configuration**
- Production deployment configuration
- Environment variable management
- Graph dependency definition
- Service integration settings

**Configuration Elements:**
- Graph dependencies and imports
- Environment file references
- Service endpoint definitions
- Debugging and monitoring settings

## 🛠️ LangSmith Setup & Configuration

### Environment Variables
Set up your environment with the necessary LangSmith configuration variables including API key, tracing enablement, project name, and endpoint URL.

### Basic Tracing Setup
Configure LangSmith tracing in your application by setting environment variables and using the traceable decorator on your agent functions to enable monitoring and debugging.

## 🔧 Debugging Workflows

### 1. State Inspection Workflow
Create debug utility functions that can inspect and log the current state at any point in your agent's execution. Add debug checkpoints as nodes in your graph to monitor state changes.

### 2. Error Handling Pattern
Implement robust error handling by wrapping agent logic in try-catch blocks. Log errors with detailed information including error type, message, timestamp, and state snapshot for comprehensive debugging.

### 3. Performance Monitoring
Use decorators to monitor function execution times and track performance metrics. Store performance data in the state to analyze bottlenecks and optimize agent performance.

## 📊 LangSmith Debugging Features

### Trace Analysis
- **Request/Response Tracking**: Monitor all LLM calls
- **Token Usage**: Track costs and usage patterns
- **Latency Analysis**: Identify performance bottlenecks
- **Error Tracking**: Capture and analyze failures

### Visualization Tools
- **Graph Flow Visualization**: See your agent's execution path
- **State Evolution**: Track how state changes over time
- **Decision Points**: Understand agent reasoning
- **Performance Heatmaps**: Identify slow components

## 🐛 Common Debugging Scenarios

### Scenario 1: Agent Loops Infinitely
**Symptoms**: Agent never reaches END state
**Debug Steps**:
1. Add state logging at each node
2. Check conditional logic in edges
3. Verify END conditions are reachable
4. Use LangSmith to trace execution path

**Solution Pattern**: Implement loop protection by tracking iteration counts and setting maximum loop limits to prevent infinite execution.

### Scenario 2: Unexpected State Changes
**Symptoms**: State contains unexpected values
**Debug Steps**:
1. Add state snapshots before/after each node
2. Use LangSmith to compare state evolution
3. Check for unintended state mutations
4. Verify type consistency

**Solution Pattern**: Create state validation functions that check for required keys and validate data types to ensure state integrity throughout execution.

### Scenario 3: LLM Call Failures
**Symptoms**: Random agent failures or inconsistent responses
**Debug Steps**:
1. Check API rate limits and quotas
2. Monitor LLM response quality in LangSmith
3. Verify prompt engineering effectiveness
4. Implement retry mechanisms

## 🎯 Best Practices for Production

### 1. Comprehensive Logging
Set up proper logging configuration with appropriate log levels. Log key information at node entry and exit points to track execution flow and identify issues.

### 2. Graceful Error Handling
Implement retry logic with exponential backoff for transient failures. Set maximum retry limits and provide meaningful error messages for permanent failures.

### 3. State Validation
Use schema validation libraries to define and validate state structure. Implement validation functions that check for required fields and proper data types before processing.

## 📈 Monitoring Metrics

### Key Metrics to Track
- **Success Rate**: Percentage of successful completions
- **Average Latency**: Time per agent execution
- **Token Usage**: Cost monitoring and optimization
- **Error Rate**: Frequency and types of errors
- **User Satisfaction**: Feedback and quality metrics

### LangSmith Dashboards
Create custom dashboards to monitor:
- Agent performance over time
- Most common error patterns
- Resource usage trends
- User interaction patterns

## 🚀 Quick Debugging Checklist

When your agent isn't working:

1. **Check Environment Variables** ✅
   - API keys are set correctly
   - LangSmith configuration is active

2. **Verify Graph Structure** ✅
   - All nodes have proper edges
   - Conditional logic is correct
   - END state is reachable

3. **Inspect State Flow** ✅
   - State updates are returning properly
   - Type consistency is maintained
   - Required keys are present

4. **Monitor LLM Calls** ✅
   - API responses are successful
   - Prompts are well-formatted
   - Rate limits are not exceeded

5. **Test Error Scenarios** ✅
   - Error handling works as expected
   - Recovery mechanisms function
   - Fallbacks are appropriate


Remember: Good debugging practices are essential for production-ready LangGraph applications. Always instrument your agents with proper logging, monitoring, and error handling!
