# 📈 Stock Picker AI Crew

This project demonstrates an **AI agent framework for financial analysis** using [CrewAI](https://crewai.com).  
Instead of a simple sequential workflow, we designed a **hierarchical crew** with a manager agent that oversees specialized agents.  
The system identifies trending companies, conducts thorough research on them, and selects the most promising investment opportunity.

---

## 🚀 Features
- **Hierarchical Process**: A manager agent assigns tasks to sub-agents instead of just sequential execution.
- **Multiple Specialized Agents**:
  - `trending_company_finder` → scans financial news for trending companies.
  - `financial_researcher` → produces detailed research reports.
  - `stock_picker` → picks the best company for investment.
  - `manager` → coordinates the overall workflow.
- **Structured Outputs**: Used Pydantic models (`TrendingCompanyList`, `TrendingCompanyResearchList`) to enforce reliable structured data.
- **Custom Tools**:
  - `SerperDevTool` for financial news search.
  - `PushNotificationTool` for real-time user updates.
- **Config Driven**: Agents and tasks defined in YAML (`agents.yaml`, `tasks.yaml`) for easy reconfiguration.
- **Extensible**: Supports passing an LLM by model name or delegating to an agent that manages sub-tasks.

---

## 🛠️ Technologies Used
- [CrewAI](https://crewai.com) – agent orchestration
- [SerperDevTool](https://serper.dev/) – news search
- [Pydantic](https://docs.pydantic.dev/) – structured output validation
- [Requests](https://requests.readthedocs.io/) – API calls
- **Push Notification Tool** – custom integration with [Pushover](https://pushover.net/)

---
## 🔹 Crew Execution Overview

### 1. Task Assignment
The manager agent assigns tasks like `find_trending_companies` and delegates work to coworkers.
![Task Assignment](crew%20works.png)

---

### 2. Crew Execution Started
The system initializes, and the **Investment Project Manager** agent begins executing the first task.
![Crew Execution Started](Crew1.png)

---

### 3. Delegations and Searches
Agents use the SerperDev tool to search the internet and return structured results, with multiple delegation steps shown.
![Delegations and Search](delegations.png)

---

### 4. Research Output
The research agent compiles findings into a detailed, structured analysis of multiple companies.
![Research Output](Feedback_about_companies.png)

---

### 5. First Final Decision Example
The crew selects **Perplexity AI** as the best company, citing specific reasons.  
Other companies like FlutterFlow and Cohere are marked as “Not Selected” with a rationale.
![Final Decision Example 1](final_decision_1.png)

---

### 6. Alternative Final Decision Example
In another run, the system selects **Supabase** as the strongest investment option, with clear reasoning and comparisons.
![Final Decision Example 2](Final_decisions.png)

## 🧠 Adding Memory to the Crew

In the updated version, we enhanced the crew with **memory modules**:
- **Short Term Memory** → Keeps track of recent interactions within a single execution.
- **Long Term Memory** → Stores knowledge in persistent SQLite storage.
- **Entity Memory** → Helps agents remember entities like company names, tickers, and contexts across runs.

This upgrade allows agents to avoid repeating results, recall previously analyzed companies, and build on past insights.

---

### 🔹 Example Run with Memory

#### 1. Memory Retrieval in Action
When starting a task, agents now query **Long Term, Short Term, and Entity Memory** before searching the internet.
![Memory Retrieval](Memory1.png)

---

#### 2. Delegation with Memory Context
The **Financial News Analyst** agent leverages both memory and Serper searches to find **new companies** not seen before.
![Delegation with Memory](memory2.png)

---

#### 3. Compiled Insights from Memory + Search
The agent produces a refined list of trending companies, enhanced by past stored results.
![Insights with Memory](Memory3.png)

---

#### 4. Final Investment Decision
The crew selects **Anthropic** as the best investment, with full rationale and clear reasoning.  
Memory ensures companies already evaluated aren’t re-selected unnecessarily.
![Final Decision with Memory](memory4.png)

---

## 📈 Why Memory Matters
- Prevents duplication (agents don’t pick the same company in repeated runs).  
- Builds continuity — the system “remembers” companies and insights across executions.  
- Strengthens decision-making by blending **retrieved memory** with **new search results**.  

This makes the Stock Picker Crew **smarter and more reliable over time**, moving closer to a real analyst assistant rather than just a stateless script.

