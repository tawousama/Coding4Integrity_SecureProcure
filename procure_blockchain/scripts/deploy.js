// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {
  const currentTimestampInSeconds = Math.round(Date.now() / 1000);

  const deadline = currentTimestampInSeconds + 3000 //for testing
  const title = "PCs and computer equipements"
  const description = ""

  //added
  const Tender = await hre.ethers.getContractFactory("Tender");
  const Bid = await hre.ethers.getContractFactory("Bid");

  const tender = await Tender.deploy(title, description, deadline);

  //console.log(tender);
  await tender.waitForDeployment();

  console.log(
    `Tender deployed to ${tender.target}`
  );

  const price = 100;
  const tenderaddress = `${tender.target}`
  const amount = 100;

  const bid = await Bid.deploy(price, amount, tenderaddress);
  
  await bid.waitForDeployment();
  console.log(
    `Bid deployed to ${bid.target}`
  );

}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
