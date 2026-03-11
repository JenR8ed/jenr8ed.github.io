module.exports = {
  darkMode: "class",
  content: ["./index.html"],
  theme: {
    extend: {
      colors: {
        "primary": "#0df20d",
        "background-light": "#f5f8f5",
        "background-dark": "#050a05",
        "terminal-black": "#020402",
        "terminal-glow": "rgba(13, 242, 13, 0.15)",
      },
      fontFamily: {
        "display": ["Space Grotesk", "sans-serif"],
        "mono": ["JetBrains Mono", "monospace"]
      },
      borderRadius: {"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"},
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
}
