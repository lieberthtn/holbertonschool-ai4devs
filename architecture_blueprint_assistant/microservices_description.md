# Microservices Architecture – CodeQuest (Technical Deep Dive)

This document outlines the 8 microservices powering the CodeQuest platform, with a specific focus on technical implementation details to ensure modularity and scalability.

## Detailed Service Specifications

1. **Identity & Access Service**: Implements OAuth2 and OpenID Connect. It issues short-lived JWT tokens and manages granular RBAC (Role-Based Access Control) to separate University Admin privileges from Student actions.
2. **University Management Service**: A multi-tenant config service that handles tenant-specific metadata, DNS mapping for subdomains, and feature flags to toggle advanced modules per university.
3. **Global Reward Service**: An event-driven ledger that aggregates pass/fail signals from the runner and peer reviews to calculate XP and update institutional leaderboards via an asynchronous message bus.
4. **Adaptive Content Service**: A headless CMS service that delivers localized curriculum assets via a GraphQL API, allowing universities to inject their own project parameters.
5. **Safe Code Runner Service**: A sandboxed execution engine using gVisor/Docker to run untrusted code. It performs static and dynamic analysis to prevent system call abuse while validating student logic.
6. **AI Behavior Analytics Service**: Uses TensorFlow-based models to analyze student interaction logs, identifying learning plateaus and automatically adjusting task difficulty vectors.
7. **Peer Assessment Service**: Implements a double-blind, randomized assignment algorithm. It manages the lifecycle of a review (Pending -> Under Review -> Validated) and uses a consensus-based scoring logic to ensure grading fairness before triggering XP rewards.
8. **Real-time Matchmaking Service**: A high-concurrency Node.js/Socket.io service that utilizes Redis Pub/Sub for sub-100ms latency. It manages elo-based matchmaking and maintains stateful WebSocket connections for live "coding battles" between students.

## Implementation & Integration
- **Service Independence**: Each service has its own dedicated PostgreSQL schema (or Redis instance for Matchmaking), preventing data coupling.
- **Inter-Service Communication**: Critical path interactions use gRPC for low latency, while non-critical updates (like rewards) are handled via RabbitMQ/Kafka events.
- **Observability**: Every service exposes Prometheus metrics to monitor the health of university-specific traffic spikes.
