// The Y2K look: glossy aqua, chrome silver and lime, on a desktop-wallpaper sky.
// The palette is fixed on purpose, it doesn't follow the Herdr theme.

export default {
  id: "y2k",
  label: "Y2K",
  art: "mods/herdr-critters/themes/y2k/art",
  // Share Tech Mono runs larger than VT323, so the name text is smaller.
  fonts: { pixel: "Orbitron", mono: "Share Tech Mono", monoSize: 15, monoLine: "18px" },
  colors: {
    bg: "#dde5ee",
    head: "#5a6f8c",
    machine: "#1e7bff",
    focus: "#1e7bff",
    text: "#0b2545",
    sub: "#4f6585",
    badgeBg: "#ffffffcc",
    idleEdge: "#8a9bb0",
    idleMark: "#33475f",
    idleBox: "#b8c6d6",
    btnEdge: "#a9b8ca",
    divider: "#c3cfdc",
    rowHover: "#0b25450d",
    clear: "#00000000",
    // Appended to a status color for the sprite box border.
    statusEdgeAlpha: "99",
  },
  // A scene per machine: this machine gets the local scene, others take the rest in turn.
  scenes: {
    bliss: { card: "#d6e6f7", edge: "#8fb4dd", box: "#5f93cf", label: "#1a4f8f" },
    ocean: { card: "#d3eef0", edge: "#7cc7cf", box: "#3aa3b0", label: "#0e6470" },
    sunset: { card: "#f6e0d6", edge: "#e0a58c", box: "#d07a5a", label: "#8f3a1a" },
    grape: { card: "#e6dcf3", edge: "#b49be0", box: "#8a6cc8", label: "#4b2a8a" },
  },
  localScene: "bliss",
  remoteScenes: ["ocean", "sunset", "grape"],
  // Chat-speak of the time.
  status: {
    working: { word: "SYNC", color: "#0a8fd6" },
    blocked: { word: "OMG!", color: "#e0115f" },
    done: { word: "W00T", color: "#2c9e1a" },
    idle: { word: "BRB", color: "#6b7d95" },
  },
  // Every agent's name, a character to follow: 4 to 7 letters each.
  names: [
    "aqua", "blip", "bling", "bubbles", "chrome", "dialup", "disco", "fizz", "flip", "frosty",
    "glossy", "gummy", "jelly", "kazoo", "laser", "lime", "mixtape", "modem", "nano", "orbit",
    "pager", "plasma", "qwerty", "skater", "techno", "tunes", "vapor", "wifi", "xtreme", "yoyo",
  ],
};
