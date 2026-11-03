// The themes the mod ships. Order is the cycle order of the header button.

import deepsea from "./deepsea/theme.js";
import edo from "./edo/theme.js";
import noir from "./noir/theme.js";
import retro from "./retro/theme.js";
import y2k from "./y2k/theme.js";

export const THEMES = [retro, edo, y2k, noir, deepsea];
export const DEFAULT_THEME = "retro";
export const themeById = (id) => THEMES.find((t) => t.id === id) ?? THEMES.find((t) => t.id === DEFAULT_THEME);
