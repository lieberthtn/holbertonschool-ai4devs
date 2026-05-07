# Microservices Architecture – CodeQuest

This architecture uses a decentralized approach with 8 distinct microservices to manage the multi-university SaaS platform.

## Service Descriptions
1. **Identity & Role Service**: Manages user authentication and specific access levels for Students and University Admins across different subdomains.
2. **Organization Service**: Handles university-specific configurations, tenant branding, and administrative settings for each institution.
3. **Gamification Service**: Processes XP, badges, and streaks. It maintains institutional leaderboards to keep students engaged.
4. **Curriculum Service**: Serves both global coding tasks and customized university projects based on the specific academic path.
5. **Code Execution Service**: An isolated environment that runs student code within secure containers to validate logic and output.
6. **AI Personalization Service**: Analyzes performance metrics to dynamically adjust the learning difficulty for each individual student.
7. **Community & Review Service**: Facilitates peer-to-peer code reviews, allowing students to provide feedback and earn community points.
8. **Battle Arena Service**: A low-latency service handling real-time competitive coding matches between users.

## Interactions & Scaling
- **Event-Driven Architecture**: The **Code Execution Service** sends asynchronous signals to the **Gamification Service** upon task completion.
- **Subdomain Routing**: The **API Gateway** (external to core logic) uses the request host header to identify the tenant and route traffic to the **Organization Service**.
- **Data Partitioning**: Each service utilizes its own database schema to ensure high availability and prevent single points of failure.
