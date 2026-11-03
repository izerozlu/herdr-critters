// The themes the mod ships. Order is the cycle order of the header button.

import retro from "./retro/theme.js";

export const THEMES = [retro];
export const DEFAULT_THEME = "retro";
export const themeById = (id) => THEMES.find((t) => t.id === id) ?? THEMES.find((t) => t.id === DEFAULT_THEME);
