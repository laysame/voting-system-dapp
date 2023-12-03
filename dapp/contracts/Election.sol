// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.4.0 < 0.9.0;
pragma abicoder v2;

contract Election {
    // The candidate model
    struct Candidate {
        string name;
        uint index;
    }

    // List of candidates
    mapping(uint => Candidate) private _candidates;

    // Vote count for each candidate
    mapping(uint => uint) private _candidateVotes;

    // Counter for assigning unique IDs to candidates
    uint public candidatesCounter;

    // List of people who cast their vote
    mapping(address => bool) public voters;

    constructor() {
        // Add the candidates for the election
        addCandidate("Cecilia Meireles");
        addCandidate("Cora Coralina");
        addCandidate("Adelia Prado");
    }

    function addCandidate(string memory name_) private  {
        _candidates[candidatesCounter] = Candidate(name_, candidatesCounter);
        candidatesCounter++;
    }

    function getCandidateByIndex(uint candidateIndex_) external view returns (Candidate memory candidate) {
        // Make sure the candidate exist
        require(candidateIndex_ >= 0 && candidateIndex_ < candidatesCounter, "Candidate index is not valid");

        candidate = _candidates[candidateIndex_];
    }

    function castVote(uint candidateIndex_) external {
        // Ensure each address only votes once
        require(!voters[msg.sender], "Address already cast a vote for the election");

        // Make sure the candidate exist
        require(candidateIndex_ >= 0 && candidateIndex_ < candidatesCounter, "Candidate index is not valid");

        _candidateVotes[candidateIndex_]++;
        voters[msg.sender] = true;
    }

    function getVoteCounts() external view returns (uint[] memory) {
        uint[] memory result = new uint[](candidatesCounter);

        for (uint i = 0; i < candidatesCounter; i++) {
            result[i] = _candidateVotes[i];
        }

        return result;
    }
}
