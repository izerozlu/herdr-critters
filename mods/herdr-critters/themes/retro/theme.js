// The retro look: every color, scene, word, font and name the view uses.
// The palette is fixed on purpose, it doesn't follow the Herdr theme.

export default {
  id: "retro",
  label: "RETRO",
  // Optional: where picked names are stored. Retro keeps its original key.
  namesKey: "names",
  art: "mods/herdr-critters/themes/retro/art",
  fonts: { pixel: "Silkscreen", mono: "VT323" },
  colors: {
    bg: "#12131b",
    head: "#6b6f82",
    machine: "#e8922e",
    focus: "#e8922e",
    text: "#f1ecff",
    sub: "#9a95b0",
    badgeBg: "#0b0b12cc",
    idleEdge: "#8a849e",
    idleMark: "#d8d2ee",
    idleBox: "#6a6380",
    btnEdge: "#34364a",
    divider: "#22232e",
    clear: "#00000000",
    // Appended to a status color for the sprite box border.
    statusEdgeAlpha: "99",
  },
  // A scene per machine: this machine gets the local scene, others take the rest in turn.
  scenes: {
    dusk: { card: "#1f1830", edge: "#3e2f5c", box: "#4b3870", label: "#b49be0" },
    den: { card: "#181d26", edge: "#2a3442", box: "#34465a", label: "#8fb3c8" },
    dawn: { card: "#221819", edge: "#4a2e2a", box: "#6a3e30", label: "#e8b48c" },
    moss: { card: "#161e19", edge: "#2a3e2e", box: "#3a5a3a", label: "#a8d890" },
  },
  localScene: "dusk",
  remoteScenes: ["den", "dawn", "moss"],
  status: {
    working: { word: "BUSY", color: "#5ee6f2" },
    blocked: { word: "HELP!", color: "#ff5a5a" },
    done: { word: "DONE", color: "#9be36a" },
    idle: { word: "IDLE", color: "#a9a3bf" },
  },
  // Every agent's name, a character to follow: 4 to 7 letters each.
  names: [
    "pixel", "byte", "nova", "rook", "ziggy", "mochi", "bolt", "echo", "juno", "kiwi",
    "luma", "miso", "nimbus", "onyx", "pepper", "quill", "rusty", "sprout", "tango", "umbra",
    "vega", "waffle", "yeti", "zephyr", "comet", "dusty", "fable", "gizmo", "hopper", "ivory",
  ],
};
