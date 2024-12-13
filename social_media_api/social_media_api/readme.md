Follow Management API:

Follow:
Endpoint: POST /follow/<user_id>/
Request Body: None
Response: { "status": "following" }
Unfollow:
Endpoint: POST /unfollow/<user_id>/
Request Body: None
Response: { "status": "unfollowed" }
Feed API:

View Feed:
Endpoint: GET /feed/
Response: List of posts authored by followed users, ordered by creation date.