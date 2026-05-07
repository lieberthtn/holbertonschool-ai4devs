# Microservices Architecture – CodeQuest (Multi-Tenant SaaS)

This architecture is optimized for a multi-university setup, where each institution operates on its own subdomain (e.g., uni-name.codequest.com) with independent administrative control.

## Key Multi-Tenant Services
- **API Gateway & Subdomain Router**: Acts as the traffic controller. It identifies the "Tenant" (University) from the subdomain and routes requests to the appropriate context.
- **Organization (Tenant) Service**: Manages university profiles, their specific settings, and global admin assignments.
- **Identity & Role Service**: Handles multi-level authentication. Distinguishes between Global Admins, University Admins, and Students.
- **University-Specific Content Service**: Allows each university to upload and manage its own unique curriculum and project rubrics.
- **Inter-University Battle Arena**: A specialized service that allows students from different universities to compete while maintaining their institutional identity.

## Multi-Tenancy Logic
- **Subdomain Isolation**: Data is filtered based on the Tenant ID identified at the Gateway level.
- **Admin Delegation**: University Admins can only manage users and content within their own assigned subdomain/tenant.
- **Curriculum Customization**: While core tasks are available, the **Content Service** allows University Admins to override or add specific modules aligned with their academic year.
