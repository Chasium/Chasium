import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue(), vueJsx()],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
    server: {
        port: 8080,
        proxy: {
            "/api": {
                target: "http://localhost:5000",
                secure: false,
                changeOrigin: false,
                rewrite: (path) => path.replace(/^\/api/, ""),
            },
        },
    },
});
