// The noir look: a 1940s detective city at night. Grays, with blood red only
// for trouble. The palette is fixed on purpose, it doesn't follow the Herdr theme.

export default {
  id: "noir",
  label: "NOIR",
  art: "mods/herdr-critters/themes/noir/art",
  // Drawn as raster PNG art (art/themes/noir, skia-python).
  artExt: "png",
  fonts: { pixel: "Silkscreen", mono: "VT323" },
  colors: {
    bg: "#101012",
    head: "#6a6a70",
    machine: "#c8c3b6",
    focus: "#f4f1e8",
    text: "#f1eee6",
    sub: "#8e8c86",
    badgeBg: "#08080acc",
    idleEdge: "#77777e",
    idleMark: "#cfcdc6",
    idleBox: "#5a5a60",
    btnEdge: "#2e2e34",
    divider: "#1e1e22",
    clear: "#00000000",
    // Appended to a status color for the sprite box border.
    statusEdgeAlpha: "99",
  },
  // A scene per machine: this machine gets the local scene, others take the rest in turn.
  scenes: {
    office: { card: "#1c1a17", edge: "#3a352c", box: "#4e473a", label: "#c8b896" },
    alley: { card: "#15181b", edge: "#2a3138", box: "#3a4550", label: "#9fb0bc" },
    precinct: { card: "#18181a", edge: "#33333a", box: "#46464e", label: "#bdbdc4" },
    records: { card: "#171a18", edge: "#2c342e", box: "#3c4840", label: "#a4b4a6" },
  },
  localScene: "office",
  remoteScenes: ["alley", "precinct", "records"],
  // Told apart by value (dim, mid, bright) and the one red.
  status: {
    working: { word: "SNOOP", color: "#f4f1e8" },
    blocked: { word: "HEAT!", color: "#e0303c" },
    done: { word: "SOLVED", color: "#a8a69e" },
    idle: { word: "QUIET", color: "#6e6e76" },
  },
  // Every agent's name, a character to follow: 4 to 7 letters each.
  names: ["spade", "bugsy", "louie", "vito", "slick", "dutch", "marlow", "velma", "rocco", "lefty", "mickey", "dolly"],
};
