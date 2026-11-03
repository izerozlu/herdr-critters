// The cyber look: neon on black, a rainy city behind every agent.
// The palette is fixed on purpose, it doesn't follow the Herdr theme.

export default {
  id: "cyber",
  label: "CYBER",
  art: "mods/herdr-critters/themes/cyber/art",
  fonts: { pixel: "Orbitron", mono: "Share Tech Mono", monoSize: 15, monoLine: "18px" },
  colors: {
    bg: "#07060d",
    head: "#6a5f8a",
    machine: "#ff2bd6",
    focus: "#00f0ff",
    text: "#e8f6ff",
    sub: "#8a86a8",
    badgeBg: "#05040acc",
    idleEdge: "#5a5078",
    idleMark: "#b8b0e0",
    idleBox: "#3a3456",
    btnEdge: "#2e2448",
    divider: "#1a1528",
    rowHover: "#00f0ff12",
    clear: "#00000000",
    // Appended to a status color for the sprite box border.
    statusEdgeAlpha: "99",
  },
  // A scene per machine: this machine gets the local scene, others take the rest in turn.
  scenes: {
    neon: { card: "#1a0a26", edge: "#4a1666", box: "#6a1a8a", label: "#ff7ae8" },
    ice: { card: "#06141f", edge: "#0f3a52", box: "#14506e", label: "#7af4ff" },
    acid: { card: "#08160c", edge: "#1a4424", box: "#236032", label: "#8aff6a" },
    amber: { card: "#1a0e05", edge: "#4a2a0c", box: "#6a3e10", label: "#ffc05a" },
  },
  localScene: "neon",
  remoteScenes: ["ice", "acid", "amber"],
  status: {
    working: { word: "HACK", color: "#00f0ff" },
    blocked: { word: "PING!", color: "#ff2e63" },
    done: { word: "SYNC", color: "#39ff14" },
    idle: { word: "AFK", color: "#7a6f9a" },
  },
  // Every agent's name, a character to follow: 4 to 7 letters each.
  names: [
    "glitch", "proxy", "cipher", "vapor", "razor", "chrome", "neon", "static", "synth", "shard",
    "kilo", "vector", "relay", "daemon", "socket", "cobalt", "rogue", "flux", "mantis", "tesla",
    "spike", "binary", "zero", "omega", "ghost", "hydra", "karma", "nitro", "pulse", "wire",
  ],
};
