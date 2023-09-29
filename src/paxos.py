import threading
import time
import random

class Proposal:
    def __init__(self, number, value):
        self.number = number
        self.value = value

class PaxosNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.proposal_number = 0
        self.accepted_proposal = None
        self.promised_proposal_number = 0
        self.leader_id = None

    def prepare(self, proposal_number, leader_id):
        if proposal_number > self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            self.leader_id = leader_id
            return self.accepted_proposal
        else:
            return None

    def accept(self, proposal):
        if proposal.number >= self.promised_proposal_number:
            self.accepted_proposal = proposal
            return True
        else:
            return False

class PaxosProposer:
    def __init__(self, proposer_id, nodes):
        self.proposer_id = proposer_id
        self.nodes = nodes
        self.proposal_number = 0

    def propose_value(self, value):
        while True:
            self.proposal_number += 1
            proposal = Proposal(self.proposal_number, value)

            # Phase 1: Prepare
            responses = [node.prepare(proposal.number, self.proposer_id) for node in self.nodes]
            highest_accepted_proposal = max(
                (resp for resp in responses if resp is not None),
                default=None,
                key=lambda p: p.number
            )
            if highest_accepted_proposal is not None:
                proposal.value = highest_accepted_proposal.value

            # Phase 2: Accept
            responses = [node.accept(proposal) for node in self.nodes]
            if responses.count(True) > len(self.nodes) / 2:
                print(f'Proposer {self.proposer_id}: Consensus achieved: {proposal.value}')
                break
            else:
                print(f'Proposer {self.proposer_id}: Failed to achieve consensus, retrying...')
                time.sleep(random.uniform(0.5, 2))  # Simulate random retry delay

# nodes = [PaxosNode(i) for i in range(5)]
# proposers = [PaxosProposer(i, nodes) for i in range(3)]

# Simulate multiple rounds of consensus with multiple proposers
# for i in range(3):
#     value = f'value-{i}'
#     threads = [threading.Thread(target=proposer.propose_value, args=(value,)) for proposer in proposers]
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#         thread.join()
#     time.sleep(1)  # Simulate network delay between rounds
