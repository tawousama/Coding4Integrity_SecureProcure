// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './Bid.sol';

contract Tender {
    address public owner;
    string public tenderTitle;
    uint256 public publishDate;
    string public tenderDescription;
    uint256 public bidDeadline;
    bool public isClosed;
    uint256 public winningBidId;

    Bid[] public bids;

    event BidSubmitted(address indexed supplier, uint256 amount, uint256 price ,uint256 bidId);
    event TenderClosed(uint256 winningBidId);

    constructor(
        string memory _title,
        string memory _description,
        uint256 _deadline
    ) {
        owner = msg.sender;
        tenderTitle = _title;
        tenderDescription = _description;
        publishDate = block.timestamp;
        bidDeadline = block.timestamp + _deadline;
        isClosed = false;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier isNotClosed() {
        require(!isClosed, "The tender is closed");
        _;
    }

    function submitBid(uint256 price, uint256 amount) public payable isNotClosed {
        require(amount > 0, "Bid amount must be greater than 0");
        Bid bid = new Bid(price,amount,owner);
        bids.push(bid);
        emit BidSubmitted(msg.sender, price, amount, bids.length - 1);
    }

    function closeTender() public onlyOwner isNotClosed {
        require(block.timestamp >= bidDeadline, "Bid deadline has not passed yet");
        require(bids.length > 0, "No bids have been submitted");
        
        uint256 winningScore = bids[0].getScore();
        for (uint256 i = 1; i < bids.length; i++) {
            if (bids[i].getScore() < winningScore) {
                winningScore = bids[i].getScore();
                winningBidId = i;
            }
        }
        
        bids[winningBidId].acceptBid();
        isClosed = true;
        emit TenderClosed(winningBidId);
    }
}