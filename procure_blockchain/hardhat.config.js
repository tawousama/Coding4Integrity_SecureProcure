require("dotenv").config();
//require("@nomiclabs/hardhat-etherscan");
require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.18",
  networks: {
    mumbai: {
      url: "https://rpc-mumbai.maticvigil.com",
      accounts: [process.env.PRIVATE_KEY]
    }  
  },
  etherscan: {
    // Your API key for Etherscan
    // Obtain one at https://etherscan.io/ or https://polygonscan.com/
    apiKey: { polygonMumbai: process.env.ETHERSCAN_API_KEY }
  }
};
