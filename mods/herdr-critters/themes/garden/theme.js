// The garden look: a cozy daytime cottage garden on a light cream background.
// The palette is fixed on purpose, it doesn't follow the Herdr theme.

export default {
  id: "garden",
  label: "GARDEN",
  art: "mods/herdr-critters/themes/garden/art",
  artExt: "png",
  fonts: { pixel: "Silkscreen", mono: "VT323" },
  colors: {
    bg: "#f6f1e0",
    head: "#7d8a6a",
    machine: "#a0522d",
    focus: "#e07aa5",
    text: "#3b3226",
    sub: "#7a6e58",
    badgeBg: "#fffaeccc",
    idleEdge: "#9a9480",
    idleMark: "#6a6450",
    idleBox: "#b8b29a",
    btnEdge: "#d6cfb4",
    divider: "#e3dcc4",
    clear: "#00000000",
    // Appended to a status color for the sprite box border.
    statusEdgeAlpha: "99",
  },
  // A scene per machine: this machine gets the local scene, others take the rest in turn.
  scenes: {
    greenhouse: { card: "#e9f0dc", edge: "#c9dbb2", box: "#a9c88e", label: "#4f8a3c" },
    barrow: { card: "#f6ead8", edge: "#e5cfb0", box: "#d4b088", label: "#a0522d" },
    seeds: { card: "#efe8f3", edge: "#d9cbe6", box: "#bca6d6", label: "#7a5aa8" },
    pond: { card: "#e4eff3", edge: "#c4dce6", box: "#9cc4d8", label: "#2f7aa8" },
  },
  localScene: "greenhouse",
  remoteScenes: ["barrow", "seeds", "pond"],
  status: {
    working: { word: "GROW", color: "#b87400" },
    blocked: { word: "WILT!", color: "#cc3b3b" },
    done: { word: "BLOOM", color: "#3d8b37" },
    idle: { word: "REST", color: "#8c8471" },
  },
  // Every agent's name, a garden critter to follow: 4 to 7 letters each.
  names: ["dotty", "buzz", "shelly", "ribbit", "nibbles", "flutter", "bramble", "wiggle", "clover", "digby", "hazel", "poppy"],
};
