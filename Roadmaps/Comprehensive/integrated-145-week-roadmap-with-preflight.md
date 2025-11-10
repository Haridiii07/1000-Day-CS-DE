# Integrated 145-Week Roadmap: Data Engineering & Foundational Computer Science (With Pre-Flight)

This roadmap is designed to integrate the rigorous **Teach Yourself Computer Science (TYCS)** curriculum with the practical skills of **Modern Data Engineering (DE)**, based on your commitment of **5 hours per day** over **858 non-Friday study days**.

**Start Date:** November 9, 2025 (Sunday) - **Pre-Flight Phase Begins**
**Total Study Days:** 858 (Non-Fridays)
**Total Study Hours:** 4,290 hours (5 hours/day)
**Estimated End Date:** Approximately April 2028 (Accounting for 2-week Prep Phase)

The plan is structured into two daily blocks: **Block A (3 hours)** for foundational CS and **Block B (2 hours)** for practical DE, with intentional overlap to reinforce learning.

---

## 🚀 PRE-FLIGHT PHASE: Confidence & Tooling (2 Weeks)

This 2-week phase is designed to be a high-impact "pre-flight" checklist, incorporating the best practices from the Reddit FAQ to build immediate coding confidence and set up the essential development environment before diving into the rigorous 143-week integrated roadmap.

**Goal:** Build immediate coding momentum, establish a disciplined routine, and set up the core DE environment.
**Duration:** 2 Weeks (10 non-Friday study days)
**Daily Commitment:** 5 hours (as per your main plan)

| Week | Day | Hours | Focus (Reddit FAQ Principle) | Activity (Immediate Action) |
| :--- | :--- | :--- | :--- | :--- |
| **Week -2** | **Day 1** | 5h | **Setup & Mindset** (Don't wait for inspiration) | **Action:** Install Python, VS Code, Git. Create your `Integrated-DE-Roadmap` GitHub repo. **Read:** The "Getting Started" and "How to Improve" sections of the Reddit FAQ. |
| | **Day 2** | 5h | **Active Learning** (Practice is essential) | **Coding:** Complete 5 easy problems on **CodingBat** (Python section) focusing on basic loops and conditionals. |
| | **Day 3** | 5h | **Problem Decomposition** (Break it down) | **Project:** Build a simple **Rock-Paper-Scissors** game in Python (command line). Focus on breaking the logic into small functions. |
| | **Day 4** | 5h | **Systematic Debugging** (Be a scientist) | **Coding:** Introduce a deliberate bug into your RPS game. Spend the 5 hours systematically finding and fixing it using print statements and logic checks. |
| | **Day 5** | 5h | **SQL Foundation** (Core skill) | **Coding:** Complete the first 10 exercises on **SQLBolt** (or similar interactive SQL tutorial) focusing on `SELECT`, `WHERE`, and `ORDER BY`. |
| **Week -1** | **Day 6** | 5h | **Advanced SQL** (Transformation is key) | **Coding:** Complete 10 exercises on **SQLBolt** focusing on `JOINs` and `GROUP BY`. |
| | **Day 7** | 5h | **Version Control** (Document Everything) | **Action:** Learn basic Git commands (`commit`, `push`, `pull`, `branch`). **Commit:** Push all code from Week -2 to your GitHub repo. |
| | **Day 8** | 5h | **Project Idea Generation** (Connect to a hobby) | **Project:** Build a simple Python script to **scrape a single piece of data** from a website (e.g., a stock price, a weather forecast). Use `requests` and `BeautifulSoup`. |
| | **Day 9** | 5h | **Tooling Integration** (Prepare for DE) | **Action:** Install **Docker**. Run a local **PostgreSQL** container using Docker. Connect your Python script from Day 8 to the PostgreSQL database. |
| | **Day 10** | 5h | **Final Prep** (Review and Consolidate) | **Review:** Re-read your code and notes from the last 9 days. **Plan:** Review the content for **Week 1 (SICP & Python)** of the main roadmap. **Final Commit:** Push all final setup and code to GitHub. |

---

## 🗺️ Roadmap Overview and Strategy

The core strategy is **Parallel Learning with Contextual Integration**. Foundational CS topics are studied in Block A, while Block B immediately applies the underlying principles using modern DE tools.

| Phase | Duration (Weeks) | TYCS Focus (Block A) | DE Focus (Block B) | Key Integration |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Foundations** | 1-16 (4 Months) | **SICP** (Programming) | **Python, SQL, Data Structures** | SICP concepts (recursion, abstraction) applied to Python/Pandas/SQL. |
| **Phase 2: Data Systems** | 17-32 (4 Months) | **Databases** (DDIA, CS 186) | **Data Modeling, dbt, PostgreSQL, Cloud Storage** | Deep dive into storage, indexing, and transactions directly applied to data warehousing (dbt). |
| **Phase 3: Performance & Scale** | 33-56 (6 Months) | **Algorithms & Distributed Systems** (Skiena, MIT 6.824) | **Apache Spark (PySpark), Kafka, Airflow** | Algorithms for optimization; Distributed Systems for understanding Spark/Kafka architecture. |
| **Phase 4: Low-Level Context** | 57-80 (6 Months) | **Architecture & OS** (CS:APP, OSTEP) | **DevOps (Docker/K8s), Performance Tuning, Cloud Compute** | Understanding hardware/OS to optimize Spark/Airflow performance and containerization. |
| **Phase 5: Systems & Language** | 81-112 (8 Months) | **Networking, Compilers, Math** | **Advanced Cloud (Azure), Real-Time Streaming, API Development** | Networking for distributed data transfer; Compilers for query engines; Math for ML/Stats. |
| **Phase 6: Mastery** | 113-143 (7 Months) | **Review & Advanced Projects** | **Final Capstone Project, Interview Prep** | Synthesis of all knowledge into a production-ready, optimized data platform. |

---

## 🤝 Integration and Separation Points

This roadmap is designed to keep the two tracks integrated for as long as possible.

| Integration Point | Phase | TYCS Concept | DE Application |
| :--- | :--- | :--- | :--- |
| **Initial Overlap** | **Phase 1** | Functional Programming (SICP) | Python Higher-Order Functions (Pandas `apply`, `map`) |
| **Core Overlap** | **Phase 2** | Database Internals (DDIA) | Data Modeling, Indexing, Query Optimization (`EXPLAIN ANALYZE`) |
| **Scaling Overlap** | **Phase 3** | Distributed Systems (MIT 6.824) | Spark Architecture (Driver/Executor), Kafka Partitions, Airflow Scaling |
| **Performance Overlap** | **Phase 4** | Computer Architecture (CS:APP) | Optimizing memory usage in PySpark, understanding cache locality for data access. |
| **Final Separation** | **Phase 5 (Week 100)** | Compilers/Math | Advanced Azure Services, Final Capstone |

The tracks begin to **formally separate** around **Week 100** (mid-Phase 5). By this point, the core TYCS subjects most relevant to DE (Databases, Distributed Systems, Algorithms) are complete. The remaining TYCS topics (Compilers, Math) become specialized deep dives, while the DE track focuses entirely on the final Capstone and job-readiness.

---

## 📅 Detailed Weekly Breakdown (Selected Weeks)

The total 4,290 hours are allocated as follows: **TYCS (2,574 hours)** and **DE (1,716 hours)**.

### PHASE 1: Foundations (Weeks 1-16)

**Note:** The main roadmap begins after the 2-week Pre-Flight Phase. The original start date of November 9, 2025, is now the start of the Pre-Flight. The main roadmap begins on **November 23, 2025**.

| Week | TYCS Focus (Block A: 15h) | DE Focus (Block B: 10h) | Integration & Project |
| :--- | :--- | :--- | :--- |
| **1-4** | **SICP Ch 1.1-1.3** (Procedures, Recursion, HOFs) | **Python Core** (OOP, Data Structures, Pandas Intro) | **Project:** Implement SICP concepts (e.g., HOFs) using Python/Pandas to process a small CSV file. |
| **5-8** | **SICP Ch 2.1-2.3** (Data Abstraction, Sequences, Symbolic Data) | **Core SQL** (Advanced JOINs, CTEs, Window Functions) | **Project:** Use SQL to model and query data structures (lists, trees) represented in a relational table. |
| **9-12** | **SICP Ch 3.1-3.3** (State, Environment Model, Mutable Data) | **Data Modeling** (Star/Snowflake Schema, SCDs) | **Project:** Design a simple data warehouse schema and use Python to load data into it. |
| **13-16** | **SICP Ch 4.1** (Metacircular Evaluator) | **PostgreSQL/DuckDB** (Setup, Indexing, Optimization) | **Project:** Build a simple Python-to-SQL query generator, applying SICP's interpreter concepts. |

### PHASE 2: Data Systems (Weeks 17-32)

| Week | TYCS Focus (Block A: 15h) | DE Focus (Block B: 10h) | Integration & Project |
| :--- | :--- | :--- | :--- |
| **17-20** | **Databases: DDIA Ch 1-3** (Foundations, Storage, Indexing) | **dbt Core** (Models, Tests, Documentation) | **Project:** Use dbt to transform data in a PostgreSQL warehouse. **Integration:** Apply DDIA's storage concepts to understand dbt's materialization strategies. |
| **21-24** | **Databases: DDIA Ch 4-5** (Transactions, Replication) | **Apache Airflow** (DAGs, Operators, TaskFlow API) | **Project:** Orchestrate the dbt pipeline using Airflow. **Integration:** Use Airflow's state management to ensure transactional integrity and idempotency. |
| **25-28** | **Databases: DDIA Ch 6-7** (Partitioning, Transactions) | **Azure Cloud Core** (ADLS Gen2, Azure Portal, Storage) | **Project:** Migrate the dbt/Airflow pipeline to run on Azure infrastructure (e.g., using Azure Blob Storage). |
| **29-32** | **Databases: CS 186** (Query Processing, Optimization) | **ETL/ELT Fundamentals** (Batch vs. Stream, Data Quality) | **Project:** Implement a data quality check using Python/dbt and integrate it into the Airflow DAG. |

### PHASE 3: Performance & Scale (Weeks 33-56)

| Week | TYCS Focus (Block A: 15h) | DE Focus (Block B: 10h) | Integration & Project |
| :--- | :--- | :--- | :--- |
| **33-40** | **Algorithms: Skiena Ch 1-8** (Analysis, DS, Sorting, Graphs, DP) | **Apache Spark (PySpark)** (RDDs, DataFrames, Spark SQL) | **Project:** Implement a complex graph algorithm (e.g., BFS/DFS) in PySpark. **Integration:** Use Skiena's analysis to optimize Spark transformations. |
| **41-48** | **Distributed Systems: MIT 6.824** (MapReduce, Raft, Consistency) | **Apache Kafka** (Producers, Consumers, Schema Registry) | **Project:** Build a simple distributed word-count using Spark and Kafka. **Integration:** Apply 6.824's consistency models to understand Kafka's guarantees. |
| **49-56** | **Distributed Systems: DDIA Ch 8-12** (Stream Processing, Batch) | **Advanced Airflow/dbt** (Sensors, Macros, CI/CD) | **Project:** Finalize a distributed, orchestrated ELT pipeline using Airflow, Spark, and dbt. |

### PHASE 4: Low-Level Context (Weeks 57-80)

| Week | TYCS Focus (Block A: 15h) | DE Focus (Block B: 10h) | Integration & Project |
| :--- | :--- | :--- | :--- |
| **57-64** | **Computer Architecture: CS:APP Ch 1-6** (Data Rep, Assembly, Memory Hierarchy) | **DevOps: Docker & Kubernetes** (Containerization, Deployment) | **Project:** Containerize the Airflow/Spark pipeline using Docker and deploy locally with Docker Compose. **Integration:** Understand how memory hierarchy affects data processing performance. |
| **65-72** | **Computer Architecture: CS:APP Ch 7-12** (Linking, Virtual Memory, Concurrency) | **Azure Synapse Analytics** (Spark Pools, Dedicated SQL Pools) | **Project:** Migrate the containerized pipeline to Azure Synapse Spark Pools. |
| **73-80** | **Operating Systems: OSTEP Ch 1-24** (Processes, Scheduling, Paging) | **Performance Tuning** (Linux tools, Spark UI, Query Profiling) | **Project:** Use OS-level tools to profile and optimize a slow Spark job. **Integration:** Apply OSTEP's scheduling concepts to understand resource allocation in Kubernetes/YARN. |

### PHASE 5: Systems & Language (Weeks 81-112)

| Week | TYCS Focus (Block A: 15h) | DE Focus (Block B: 10h) | Integration & Project |
| :--- | :--- | :--- | :--- |
| **81-88** | **Networking: Kurose & Ross Ch 1-4** (App, Transport, Network Layers) | **API Development** (FastAPI, Uvicorn, Data Serving) | **Project:** Build a FastAPI web service to serve data from the Synapse warehouse. **Integration:** Understand how TCP/IP affects data transfer latency in distributed systems. |
| **89-96** | **Networking: Kurose & Ross Ch 5-8** (Link, Security) | **Azure Data Factory (ADF)** (Pipelines, Mapping Data Flows) | **Project:** Rebuild the Airflow orchestration using ADF for a fully cloud-native solution. |
| **97-104** | **Compilers: Crafting Interpreters Ch 1-12** (Scanning, Parsing, AST) | **Advanced Streaming** (Azure Stream Analytics, Event Hub) | **Project:** Build a simple domain-specific language (DSL) for data transformation. **Integration:** Apply compiler concepts to understand how Spark/SQL query engines work. |
| **105-112** | **Math for CS: MIT 6.042J** (Proofs, Probability, Linear Algebra) | **Data Quality & Governance** (Great Expectations, Data Lineage) | **Project:** Implement a statistical data quality check using probability concepts. |

### PHASE 6: Mastery & Job Readiness (Weeks 113-143)

| Week | TYCS Focus (Block A: 15h) | DE Focus (Block B: 10h) | Goal |
| :--- | :--- | :--- | :--- |
| **113-120** | **Compilers/Math** (Completion) | **Final Capstone Design** (Architecture, Tool Selection) | **Design:** Create a comprehensive architecture document for the final capstone. |
| **121-130** | **TYCS Review** (CS:APP, DDIA, 6.824) | **Final Capstone Build** (Implementation, Deployment) | **Build:** Implement the end-to-end, production-ready data platform. |
| **131-143** | **Advanced Topics & LeetCode** (System Design Prep) | **Interview Preparation** (Mock Interviews, Portfolio Finalization) | **Launch:** Finalize portfolio, practice system design and behavioral interviews. |

---

## 🛠️ Weekly Study Structure (5 Hours/Day)

| Time Block | Duration | Focus | Activity Type |
| :--- | :--- | :--- | :--- |
| **Block A: TYCS** | 3 hours | Foundational CS | Reading, Lecture Videos, Exercises, Deep Thinking |
| **Block B: DE** | 2 hours | Practical Data Engineering | Coding, Tool Setup, Project Work, Documentation, LeetCode |

**Note:** Fridays are designated as a rest day, but can be used as a **catch-up day** if needed.

---

## 🎯 Milestones and Assessment

| Milestone | Target Week | Focus | Assessment |
| :--- | :--- | :--- | :--- |
| **M1: Foundational Coding** | 16 | SICP Ch 1-4, Python/SQL Mastery | **Project:** End-to-end ETL pipeline (Python/SQL) with a clean, documented codebase. |
| **M2: Data Systems Expert** | 32 | Databases (DDIA), Data Modeling, dbt, Airflow | **Project:** Orchestrated ELT pipeline (Airflow + dbt) on a cloud database. |
| **M3: Scaling Engineer** | 56 | Algorithms, Distributed Systems, Spark, Kafka | **Project:** Distributed streaming pipeline (Kafka + Spark) with performance optimization. |
| **M4: Production Ready** | 80 | Architecture, OS, DevOps (Docker/K8s), Azure Synapse | **Project:** Containerized, cloud-deployed pipeline on Azure Synapse. |
| **M5: Full Stack Data** | 112 | Networking, Compilers, Math, ADF, FastAPI | **Project:** Data serving API and a fully cloud-native orchestration solution (ADF). |
| **M6: Job Readiness** | 143 | Full Curriculum Review, Capstone | **Deliverable:** Production-ready Capstone Project and a polished portfolio/GitHub. |

This integrated roadmap provides the depth of a world-class CS education while ensuring you are building practical, job-ready skills from day one. Good luck with your journey! 🚀
