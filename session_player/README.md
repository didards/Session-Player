
# Question
Design and implement a player session service using Python and Cassandra. You are free to use any
external libraries you see fit.
Player Session Service
Your task is to design and implement a player session service which consumes events and provides
metrics about players sessions. Each user will generate two events, one start event when the session
starts and one end event when session is finished. When both events have been received the session is
considered complete. Service is expected to handle massive amount of sessions.

## Requirements
-Use Python and Cassandra
-All endpoints are REST APIs
-API for receiving event batches (1-10 events / batch)
-API for fetching session starts for the last X (X is defined by the user) hours for each country
-API for fetching last 20 complete sessions for a given player
-Data older than 1 year should be discarded

## Events
### Example start event

{
"event": "start",
"country": "FI",
"player_id": "0a2d12a1a7e145de8bae44c0c6e06629",
"session_id": "4a0c43c9-c43a-42ff-ba55-67563dfa35d4",
"ts": "2016-12-02T12:48:05.520022"
}

### Example end event

{
"event": "end",
"player_id": "0a2d12a1a7e145de8bae44c0c6e06629",
"session_id": "4a0c43c9-c43a-42ff-ba55-67563dfa35d4",
"ts": "2016-12-02T12:49:05.520022"
}

## TODO
- Once API starts working switch from Sqlite to Cassandra
- Write a seperate blog post detailing issues about cassandra
