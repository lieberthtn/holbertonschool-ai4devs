# Microservices Architecture – CodeQuest (Full SaaS Model)

This architecture supports a multi-university environment using a highly decoupled microservices approach. Each service is independently scalable and responsible for a specific business domain.

## Core Services & Descriptions
- **API Gateway & Subdomain Router**: The central entry point. It extracts the university ID from the subdomain (e.g., mdu.codequest.com) and routes traffic accordingly.
- **Organization Service**: Manages university-level settings, branding, and administrative hierarchies for each tenant.
- **Identity Service**: Handles authentication and role-based access control (RBAC), distinguishing between students, university admins, and global moderators.
- **Gamification Service**: Processes all rewards, badges, and leaderboards. It ensures that students only compete within their university rankings unless otherwise specified.
- **Learning Content Service**: Manages the curriculum, storing both global programming tasks and university-specific customized projects.
- **Code Execution Service**: An isolated, containerized environment that runs student code securely and validates results against test cases.
- **AI Personalization Service**: Analyzes student performance logs to adapt the learning curve, suggesting specific topics where the student needs improvement.
- **Social Review Service**: Facilitates the peer-review process where students can give and receive feedback on their code implementations.
- **Battle Arena Service**: A real-time WebSocket service that enables live coding competitions between students of the same or different universities.

## Multi-Tenancy & Interaction Logic
- **Data Isolation**: While services are shared, data is logically partitioned by University ID at the database level to ensure privacy.
- **Asynchronous Communication**: Major events, like completing a "Quest," are broadcasted via an event bus to trigger updates in the **Gamification** and **AI** services without blocking the user.
