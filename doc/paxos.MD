# SIMPLE PAXOS IMPLEMENTATION

- ```PaxosNode``` simulates a node in the ```Paxos``` network and implements prepare and accept methods, distinguished by ```node_id```.
- ```PaxosProposer``` is the entity attempting to propose a value to the ```Paxos``` network, distinguished by ```proposer_id``` 
- The ```propose_value``` method demonstrates the two phases of Paxos:
In Phase 1 (Prepare), multiple ```PaxosProposer``` instances launch their ```propose_value``` method in a separate thread, to simulate concurrent proposing.
In Phase 2 (Accept), if the majority of nodes respond positively to the ```prepare``` requests, the ```proposer```s sends the ```accept``` requests to all nodes. The consensus attempt is wrapped in a ```while True``` loop, so that if consensus is not achieved, the proposers will wait for a random delay and then retry.

TODO: Handle failure scenarios, 
TODO: Better control on retries, timeouts, leader election, and multiple proposers.