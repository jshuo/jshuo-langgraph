## Agentic RAG (Definition)

Agentic RAG is an advanced AI system that incorporates **AI agents** into the **RAG workflow** to control the language model’s **retrieval** and **response generation**.

### How it differs from traditional RAG
- **Traditional RAG:** retrieves information and generates responses in a more **single-step / single-pass** flow.
- **Agentic RAG:** has **AI agents** control a **multi-stage** process, enabling more **precise** and **adaptable** information retrieval.

### Key capabilities (when retrieval is insufficient)
If a retrieval step yields poor or insufficient information, the RAG agent can:
- **reformulate** queries
- **retry** with a different approach
- **seek** additional sources
- **request clarification**

### Single-agent vs multi-agent
- **Single-agent RAG:** often used in **customer support** (e.g., retrieve tracking data from a database + call a shipping API for real-time updates).
- **Multi-agent RAG:** a **modular, scalable** design that uses multiple specialized agents to handle different query types and manage complex tasks concurrently.

### Where agents are used most often
Although agents can be incorporated into different stages of the LLM RAG pipeline, **agentic RAG most commonly refers to using agents in the retrieval component**.

### How to build an agentic RAG pipeline
Common approaches include:
- a **language model with function calling**, or
- an **agent framework**

With tool access, a retrieval agent can **route queries to specialized knowledge sources**, run **multi-step retrieval**, and perform **validation** to improve reliability.

### Why it’s useful
Agentic RAG combines:
- the **reasoning + action** capabilities of AI agents, and
- the **information retrieval** strengths of RAG

to enhance **contextual understanding** and improve **response generation**.

### FAQ-style summary
While standard RAG retrieves information and passes it directly to an LLM, **Agentic RAG** allows an AI agent to intelligently decide:
- **what** to retrieve,
- **when** to retrieve it, and
- **how** to use it in **multi-step reasoning**.

## Agentic RAG: Overview (Markdown Version)

There are **six revolutionary types of Agentic RAG systems** where **AI decides what to retrieve**.

**Agentic RAG** introduces **AI agents** into the RAG workflow to control the language model’s **retrieval** and **response generation**. These systems can contain one or more types of AI agents, such as **query planning agents**.

---

## What is Agentic RAG?

**Agentic RAG** is the use of **AI agents** to facilitate **Retrieval-Augmented Generation (RAG)**.

Agentic RAG systems add AI agents to the RAG pipeline to increase **adaptability** and **accuracy**. Compared to traditional RAG systems, agentic RAG allows large language models (LLMs) to:

- conduct information retrieval from **multiple sources**
- handle **more complex workflows**

---

## How does Agentic RAG work?

Agentic RAG works by incorporating **one or more types of AI agents** into RAG systems.

Agentic RAG systems can contain one or more types of AI agents, such as:

- **Query planning agents** — the task managers of the RAG pipeline  
  - Using one agent to manage other AI models is a type of **AI orchestration**.

---

## Core Idea (Paradigm Shift)

Agentic RAG enables retrieval to become an intelligent, autonomous process:

> Agentic RAG flips the paradigm by giving the AI **agency** — the ability to reason about **what** to retrieve, **when** to retrieve it, **how** to combine sources, and **whether** to retrieve at all.

---

## What makes Agentic RAG different?

If a retrieval step yields **poor or insufficient** information, RAG AI agents can:

- reformulate queries
- retry with a different approach
- seek out more sources
- request clarification

---

## Examples / Use Cases

### Single-agent RAG
- **Use case:** Customer support  
  - Retrieve tracking details from a database  
  - Call a shipping API for real-time updates  
  - Provide delivery status

### Multi-agent RAG
A modular and scalable design for managing complex tasks simultaneously using multiple specialized agents (e.g., different query types).

---

## Agentic RAG vs Traditional RAG

- **Agentic RAG:** An AI agent controls a **multi-stage** process (plan → retrieve → evaluate → retry/refine → generate).
- **Traditional RAG:** Retrieves information and generates responses in a **single step**.
