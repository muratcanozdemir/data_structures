# RAFT - Consensus building

This is my attempt at implementing RAFT from scratch. 
To learn more about Raft and see a complete implementation, you might consider looking at existing Raft implementations in Python, such as pyraft. There's also a [visualization tool](http://thesecretlivesofdata.com/raft/) that can help you understand how Raft works.

For a full understanding, you'll want to read the [original Raft paper](https://raft.github.io/raft.pdf).

- Each ```RaftNode``` initializes with a randomized election_timeout to trigger elections.
- The ```receive_message```  method checks for the ```partitioned``` property, handles incoming ```request_vote``` and ```append_entries``` messages. If a candidate receives votes by receiving a ```vote_response``` message  from a majority of the nodes, it transitions to the leader state by calling ```become_leader```.
- The ```send_message``` method is used to send in the vote.
- The ```become_candidate``` method resets the ```election_timeout``` 
-  ```request_votes``` method, which is called from ```become_candidate```, requests the votes.
- The ```become_leader``` method starts the process of sending heartbeats by invoking ```send_heartbeats```.
- The ```send_heartbeats``` method sends heartbeat messages to all other nodes as long as the node remains in the leader state. This example sends heartbeats every 1 second for simplicity.
- A ```handle_vote_request``` method has been added to handle vote requests, granting a vote if the node hasn't voted in the current term.
- The ```handle_append_entries``` method checks the term of the incoming message. If the term of the message is greater or equal to the current term, the node reverts to the follower state and updates its term to match the leader's term, if necessary. It also resets its election timeout to prevent transitioning to the candidate state prematurely.

At the end of the script, a separate thread is started to simulate an election timeout on one of the nodes, triggering a candidate election. If you want to test network partition, you can use `simulate_network_partition` function.