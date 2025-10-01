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

