export const RPC_URL = "https://sepolia.infura.io/v3/e0147d99ceeb41e1835d2e09f4d4ce27";
export const CONTRACT_ADDRESS = "0x1D67D3511BEDd04208D419fcf559CC5f5975edEf";
export const EXPECTED_CHAIN_ID = 11155111;
export const EXPECTED_CHAIN_ID_HEX = "0xaa36a7";
export const NETWORK_NAME = "Sepolia Test Network";
export const EXPLORER_BASE_URL = "https://sepolia.etherscan.io";

export const CONTRACT_ABI = [
  {
    "inputs": [
      { "internalType": "string", "name": "_name", "type": "string" },
      { "internalType": "string[]", "name": "_interests", "type": "string[]" },
      { "internalType": "string[]", "name": "_goals", "type": "string[]" }
    ],
    "name": "register",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "anonymous": false,
    "inputs": [
      { "indexed": true, "internalType": "address", "name": "wallet", "type": "address" },
      { "indexed": false, "internalType": "string", "name": "name", "type": "string" },
      { "indexed": false, "internalType": "string[]", "name": "interests", "type": "string[]" },
      { "indexed": false, "internalType": "string[]", "name": "goals", "type": "string[]" },
      { "indexed": false, "internalType": "uint256", "name": "registeredAt", "type": "uint256" }
    ],
    "name": "UserRegistered",
    "type": "event"
  },
  {
    "inputs": [{ "internalType": "address", "name": "_user", "type": "address" }],
    "name": "fetch",
    "outputs": [
      { "internalType": "address", "name": "wallet", "type": "address" },
      { "internalType": "string", "name": "name", "type": "string" },
      { "internalType": "string[]", "name": "interests", "type": "string[]" },
      { "internalType": "string[]", "name": "goals", "type": "string[]" },
      { "internalType": "uint256", "name": "registeredAt", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "fetchAll",
    "outputs": [
      {
        "components": [
          { "internalType": "address", "name": "wallet", "type": "address" },
          { "internalType": "string", "name": "name", "type": "string" },
          { "internalType": "string[]", "name": "interests", "type": "string[]" },
          { "internalType": "string[]", "name": "goals", "type": "string[]" },
          { "internalType": "uint256", "name": "registeredAt", "type": "uint256" },
          { "internalType": "bool", "name": "exists", "type": "bool" }
        ],
        "internalType": "struct EventUsers.User[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
] as const;

export const SKILL_SUGGESTIONS = [
  "AI",
  "Web3",
  "Rust",
  "Blockchain",
  "Solidity",
  "LLM",
  "DAO",
  "ZK-SNARKS",
  "DeFi",
  "Wasm",
  "Identity",
  "Tokenomics",
  "Security"
];

export const HEADER_NAV: Array<{ id: "team" | "solutions" | "blog"; label: string }> = [
  { id: "team", label: "Your Team" },
  { id: "solutions", label: "Solutions" },
  { id: "blog", label: "Blog" }
];

export const SIDEBAR_NAV: Array<{ id: "home" | "matches" | "connections" | "saved" | "settings"; icon: string; label: string }> = [
  { id: "home", icon: "dashboard", label: "Dashboard" },
  { id: "matches", icon: "auto_awesome", label: "Matches" },
  { id: "connections", icon: "people", label: "Connections" },
  { id: "saved", icon: "bookmark", label: "Saved" },
  { id: "settings", icon: "settings", label: "Settings" }
];
