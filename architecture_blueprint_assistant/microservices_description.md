# Microservices Architecture – CodeQuest (Technical Specifications)

This architecture consists of 8 highly specialized, non-overlapping services designed for a multi-tenant university ecosystem.

## Specialized Service Descriptions
1. **Identity & Access Service**: Handles cryptographic authentication and JWT issuance. It manages cross-university security policies and verifies Global vs. Local admin tokens.
2. **University Management Service**: Strictly manages tenant-level metadata, including custom subdomains, institutional branding colors, and university-specific feature toggles.
3. **Global Reward Service**: A specialized ledger service that calculates complex gamification logic (XP, Gems, Streaks) based on incoming events from other services.
4. **Adaptive Content Service**: Manages the versioning and delivery of curriculum assets. It maps specific projects to the academic calendar of individual universities.
5. **Safe Code Runner Service**: Uses gRPC and Docker/Podman containers to execute untrusted code in sub-millisecond isolated environments for instant validation.
6. **AI Behavior Analytics Service**: Implements machine learning models to monitor user learning patterns and predict churn or identify topics where students struggle.
7. **Peer Assessment Service**: Manages the logic for double-blind code reviews, ensuring students provide constructive feedback before receiving credit for tasks.
8. **Real-time Matchmaking Service**: A high-concurrency WebSocket server designed for millisecond-latency during live competitive coding "duels" between students.

## System Interaction Details
- **Decoupled Workflow**: The **Safe Code Runner** does not know who the user is; it only validates code. It sends a generic success event to the **Global Reward Service**, which then looks up the user identity to award XP.
- **Dynamic Routing**: The **API Gateway** queries the **University Management Service** to resolve tenant context before forwarding any business-logic requests.
- **Data Integrity**: Each service maintains a strictly isolated database to prevent "noisy neighbor" effects where one university's high load could impact another's data access.
