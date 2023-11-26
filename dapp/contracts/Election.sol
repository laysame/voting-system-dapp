// SPDX-License-Identifier: GPL-3.0

pragma solidity >= 0.4.0 < 0.9.0;

contract Election {
     // Model a Candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    // Read/write candidate
    string public candidate;

    // Constructor
    function election () public {
        candidate = "Candidate 1";
    }
}