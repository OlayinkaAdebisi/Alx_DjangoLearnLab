API Documentation Update
1. Model Changes: CustomUser
We have updated the CustomUser model to handle social connections efficiently.

Field Removed: followers (redundant).

Field Added/Updated: following

Type: ManyToManyField('self')

Purpose: Tracks who the user is following.

Reverse Relationship: Django automatically creates a .followers list for the other user using related_name='followers'.

Data Structure Example:

Python

# If User A follows User B:
UserA.following.all() # Contains [User B]
UserB.followers.all() # Contains [User A]
2. New Endpoints
A. Follow a User
Allows the logged-in user to follow another user.

URL: /api/follow/<int:pk>/

Method: POST

Auth Required: Yes (Token/Session)

URL Parameters: | Parameter | Type | Description | | :--- | :--- | :--- | | pk | Integer | The unique ID of the user you want to follow. |

Success Response (200 OK):

JSON

{
    "message": "You are now following zadi_dev"
}
Error Responses:

400 Bad Request: "You cannot follow yourself."

401 Unauthorized: Authentication credentials were not provided.

404 Not Found: User with that ID does not exist.

B. Unfollow a User
Allows the logged-in user to stop following another user.

URL: /api/unfollow/<int:pk>/

Method: POST

Auth Required: Yes

URL Parameters: | Parameter | Type | Description | | :--- | :--- | :--- | | pk | Integer | The unique ID of the user you want to unfollow. |

Success Response (200 OK):

JSON

{
    "message": "You have now unfollowed zadi_dev"
}
C. Access User Feed
(Note: Ensure you have created the FeedView for this to work. This documents the standard pattern.)

Retrieves posts from only the people the current user follows.

URL: /api/feed/

Method: GET

Auth Required: Yes

Success Response (200 OK):

JSON

[
    {
        "id": 101,
        "author": "zadi_dev",
        "content": "Just deployed my new API!",
        "created_at": "2025-12-13T14:30:00Z"
    },
    {
        "id": 102,
        "author": "another_user",
        "content": "Learning Django is fun.",
        "created_at": "2025-12-13T12:00:00Z"
    }
]
3. How to Test (Quick Guide)
Using Postman or cURL:

Login first to get your Token (or log in via Admin panel for Session auth).

To Follow:

Find the ID of a user (e.g., ID 5).

Send a POST request to https://your-app.onrender.com/api/follow/5/.

Header: Authorization: Token <your_token_here> (if using tokens).

To Verify:

Check your admin panel or hit the /api/feed/ endpoint to see if their posts appear.