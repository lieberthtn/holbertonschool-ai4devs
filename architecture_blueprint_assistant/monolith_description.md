# Monolithic Architecture – CodeQuest

In this monolithic design, all core business logic is bundled into a single deployable unit. This simplifies initial development and deployment but requires scaling the entire system even if only one module is under heavy load.

## Components
- **Web & Mobile Frontend**: The interactive user interface where learners write code and view their progress.
- **Auth & Session Module**: Handles user registration, corporate identity verification, and security tokens.
- **Gamification Engine**: Manages XP, levels, daily streaks, and the global leaderboard.
- **AI Adaptive Learning Path**: Analyzes user performance data to customize the difficulty and sequence of challenges.
- **Code Execution Sandbox**: Provides a secure, isolated environment to run and validate user-submitted code snippets.
- **Curriculum Manager**: Stores the repository of coding tasks, project instructions, and video content.
- **Peer Review System**: Manages the workflow for users to submit code for feedback and rewards.
- **Battle Arena Module**: A real-time competitive module where users solve logic puzzles against each other.
- **Central Database**: A unified database (e.g., PostgreSQL) that stores all user profiles, code history, and game state.
