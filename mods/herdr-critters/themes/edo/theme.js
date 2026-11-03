// The edo look: an ukiyo-e woodblock print on washi paper, with food and
// objects as the critters. The palette is fixed on purpose, it doesn't follow the Herdr theme.

export default {
  id: "edo",
  label: "EDO",
  art: "mods/herdr-critters/themes/edo/art",
  // A print serif for labels and a brush script for names, both cut to the Latin letters.
  fonts: { pixel: "Shippori Mincho", mono: "Yuji Syuku" },
  colors: {
    bg: "#efe6d0",
    head: "#8a7a5e",
    machine: "#c23b22",
    focus: "#c23b22",
    text: "#1e2a44",
    sub: "#6e6452",
    badgeBg: "#fbf5e6cc",
    idleEdge: "#9a8e74",
    idleMark: "#4a4234",
    idleBox: "#b0a486",
    btnEdge: "#cdbf9e",
    divider: "#ddd0b2",
    rowHover: "#0000000d",
    clear: "#00000000",
    // Appended to a status color for the sprite box border.
    statusEdgeAlpha: "99",
  },
  // A scene per machine: this machine gets the local scene, others take the rest in turn.
  scenes: {
    fuji: { card: "#e4e2dc", edge: "#b8c2d0", box: "#3a5a82", label: "#24406a" },
    sakura: { card: "#f0e0da", edge: "#dcb4b4", box: "#c87a8a", label: "#a8505e" },
    take: { card: "#e4e6d2", edge: "#bccaa0", box: "#5a7a3a", label: "#3e5a26" },
    kaki: { card: "#f0e2cc", edge: "#dcbc94", box: "#c87a3a", label: "#8a4a1e" },
  },
  localScene: "fuji",
  remoteScenes: ["sakura", "take", "kaki"],
  status: {
    working: { word: "BUSY", color: "#2d5a86" },
    blocked: { word: "HELP!", color: "#c8302a" },
    done: { word: "DONE", color: "#4f7a2e" },
    idle: { word: "IDLE", color: "#8a8070" },
  },
  // Every agent's name, a character to follow: 4 to 7 letters each.
  names: [
    "onigiri", "sushi", "dango", "mochi", "ramen", "tofu", "taiyaki", "matcha", "gyoza", "bento",
    "tempura", "wasabi", "sake", "udon", "natto", "yuzu", "miso", "senbei", "anpan", "tamago",
    "kokeshi", "daruma", "chochin", "geta", "sensu", "furin", "kendama", "torii", "kasa", "maneki",
  ],
};
