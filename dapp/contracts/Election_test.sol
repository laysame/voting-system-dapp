import "remix_tests.sol"; // this import is automatically injected by Remix.
import "hardhat/console.sol";

import "../contracts/Election.sol";

contract ElectionTest {
    Election election;

    function beforeAll() public {
        election = new Election();
    }

    function canGetCandidateByIndex() public {
        Assert.equal(election.getCandidateByIndex(0).name, string("Cecilia Meireles"), "First candidate does not match");
        Assert.equal(election.getCandidateByIndex(1).name, string("Cora Coralina"), "Second candidate does not match");
        Assert.equal(election.getCandidateByIndex(2).name, string("Adelia Prado"), "Third candidate does not match");
    }

    function canCastVoteOnlyOnce() public {
        election.castVote(0);
        election.castVote(0);
    }

    function canGetVoteCounts() public view {
        election.getVoteCounts();
    }
}