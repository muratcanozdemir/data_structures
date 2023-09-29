import threading
import time
import random

class RaftNode:
    def __init__(self, node_id, peer_nodes):
        self.node_id = node_id
        self.peer_nodes = peer_nodes
        self.state = "follower"
        self.term = 0
        self.vote_count = 0
        self.voted_for = None
        self.commit_index = 0
        self.last_applied = 0
        self.partitioned = False
        self.log = []
        self.reset_election_timeout()

    def reset_election_timeout(self):
        self.election_timeout = time.time() + random.uniform(1, 2)  # Randomized timeout

    def send_message(self, message):
        if self.partitioned:
            return
        for peer_node in self.peer_nodes:
            if not peer_node.partitioned:  # Only send message to non-partitioned nodes
                peer_node.receive_message(message)

    def receive_message(self, message):
        if self.partitioned:
            return
        
        msg_type = message.get('type')
        term = message.get('term', 0)

        if term > self.term:
            self.term = term
            self.become_follower()

        if msg_type == 'request_vote':
            self.handle_vote_request(message)
        if message['type'] == 'vote_response' and self.state == 'candidate':
            if message['vote_granted']:
                self.vote_count += 1
                if self.vote_count > len(self.peer_nodes) / 2:
                    self.become_leader()
        elif msg_type == 'append_entries':
            self.handle_append_entries(message)

    def become_candidate(self):
        self.state = "candidate"
        self.term += 1
        self.voted_for = self.node_id
        self.vote_count = 1  # Vote for self
        self.reset_election_timeout()
        self.request_votes()

    def request_votes(self):
        self.send_message({"type": "request_vote", "term": self.term, "candidate_id": self.node_id})

    def handle_vote_request(self, message):
        candidate_id = message.get('candidate_id')

        if self.voted_for is None or self.voted_for == candidate_id:
            self.voted_for = candidate_id
            self.send_message({"type": "vote_response", "term": self.term, "vote_granted": True})


    def become_leader(self):
        self.state = "leader"
        self.send_heartbeats()

    def send_heartbeats(self):
        while self.state == "leader":
            for peer_node in self.peer_nodes:
                prev_log_index = len(self.log) - 1
                prev_log_term = self.log[prev_log_index]['term'] if self.log else 0
                entries = self.log[self.commit_index + 1:]
                message = {
                    "type": "append_entries",
                    "term": self.term,
                    "leader_id": self.node_id,
                    "prev_log_index": prev_log_index,
                    "prev_log_term": prev_log_term,
                    "entries": entries,
                    "leader_commit": self.commit_index,
                }
                peer_node.receive_message(message)
            time.sleep(1)  # Send heartbeats every 1 second

    def become_follower(self):
        self.state = "follower"
        self.reset_election_timeout()

    def handle_vote_request(self, message):
        candidate_id = message.get('candidate_id')

        if self.voted_for is None or self.voted_for == candidate_id:
            self.voted_for = candidate_id
            self.send_message({"type": "vote_response", "term": self.term, "vote_granted": True})

    def handle_append_entries(self, message):
        leader_term = message.get('term')
        if leader_term >= self.term:
            self.term = leader_term
            self.become_follower()  # Revert to follower if the message term is greater or equal
            self.reset_election_timeout()

        entries = message.get('entries', [])
        prev_log_index = message.get('prev_log_index')
        prev_log_term = message.get('prev_log_term')

        if not entries:
            # Heartbeat, update commit index if necessary
            leader_commit = message.get('leader_commit')
            self.commit_index = max(self.commit_index, leader_commit)
        else:
            # Log replication
            if prev_log_index == len(self.log) - 1 and (not self.log or self.log[-1]['term'] == prev_log_term):
                self.log.extend(entries)
                if message.get('leader_commit', 0) > self.commit_index:
                    self.commit_index = min(message['leader_commit'], len(self.log) - 1)
                    self.apply_log_entries()

    def apply_log_entries(self):
        while self.last_applied < self.commit_index:
            self.last_applied += 1
        print("Applying log entry: ", self.log[self.last_applied])

# # Define peer nodes
# peer_nodes = [RaftNode(i, []) for i in range(5)]
# nodes = [RaftNode(i, peer_nodes) for i in range(5)]
# peer_nodes = nodes.copy()

# # Assign peer nodes to each node
# for node in peer_nodes:
#     node.peer_nodes = [peer for peer in peer_nodes if peer is not node]

# def simulate_network_partition(nodes, partitioned_nodes):
#     for node in nodes:
#         node.partitioned = node in partitioned_nodes

# # Simulate election timeout for one of the nodes to trigger election
# def simulate_election_timeout(node):
#     while node.state != "leader":
#         if time.time() > node.election_timeout:
#             node.become_candidate()
#         time.sleep(0.1)

# simulate_network_partition(nodes, partitioned_nodes=[nodes[0], nodes[1], nodes[2]])
# threading.Thread(target=simulate_election_timeout, args=(peer_nodes[0],)).start()
# simulate_network_partition(nodes, partitioned_nodes=[])

