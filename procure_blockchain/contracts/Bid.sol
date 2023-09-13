// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Tender.sol";

contract Bid {
    address public supplier;
    //address public customer;
    uint256 public price;
    uint256 public amount;
    uint256 public score = 0;
    bool public isAccepted;
    address public tenderAddress;

    constructor(uint256 _price, uint256 _amount, address _tenderAddress) {
        supplier = msg.sender;
        price = _price;
        isAccepted = false;
        tenderAddress = _tenderAddress;
        amount = _amount;
    }

    function getScore() public view returns (uint256) {
        return score;
    }

    function getPrice() public view returns (uint256) {
        return price;
    }

    function getAmount() public view returns (uint256) {
        return amount;
    }

    modifier onlyTenderOwner() {
        require(
            msg.sender == Tender(tenderAddress).owner(),
            "Only the tender owner can score/accept this bid"
        );
        _;
    }

    function scoreBid(uint256 _score) public onlyTenderOwner {
        score = _score;
    }

    function acceptBid() public onlyTenderOwner {
        require(!isAccepted, "Bid has already been accepted");
        isAccepted = true;
    }

    
}