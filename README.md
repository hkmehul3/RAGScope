
# RAGScope

Production-grade Retrieval-Augmented Generation (RAG) platform with:
- Eval Framework
- Granular Tracing
- Observability
- Cost Monitoring
- Stateful Agent Workflows

## Tech Stack
- FastAPI
- LangGraph
- PostgreSQL
- Azure Monitor
- Docker
- GitHub Actions

## Features
- Async RAG Pipeline
- Eval Pipelines
- Token Usage Monitoring
- Latency Tracking
- Cost-per-request Metrics
- Granular State Tracing
- Observability Dashboard

## Run Locally

```bash
docker-compose up --build
```

## Architecture

User Query
→ FastAPI Gateway
→ LangGraph Workflow
→ Retriever
→ Vector DB
→ LLM Generation
→ Eval Engine
→ Tracing + Metrics
→ Dashboard
