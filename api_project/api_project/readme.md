## Authentication Setup

1. **Retrieve Token**:
   - Endpoint: `POST /auth/token/`
   - Payload:
     ```json
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```
   - Response:
     ```json
     {
         "token": "your_generated_token"
     }
     ```

2. **Use Token**:
   - Add the following header to authenticated requests:
     ```
     Authorization: Token your_generated_token
     ```

## Permissions

- The `BookViewSet` enforces authentication using `IsAuthenticated`.
- Admin users can perform all CRUD operations, while non-admin users can only read (`GET`) data.
