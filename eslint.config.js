import js from "@eslint/js";
import globals from "globals";
import pluginReact from "eslint-plugin-react";
import { defineConfig } from "eslint/config";

const cleanGlobals = Object.fromEntries(
  Object.entries(globals.browser).filter(
    ([key]) => !key.includes("AudioWorkletGlobalScope")
  )
);

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,jsx}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: {
      globals: cleanGlobals,
    },
  },
  pluginReact.configs.flat.recommended,
]);
