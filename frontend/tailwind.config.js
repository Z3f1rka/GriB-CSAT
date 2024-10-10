/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./pages/**/*.{js,jsx,vue}",
    "./components/**/*.{js,jsx,vue}",
    "./app/**/*.{js,jsx,vue}",
    "./src/**/*.{js,jsx,vue}",
  ],
  theme: {
    extend: {
      colors: { main: "#01bb72", secondary: "#074444", tgray: "#50525B" },
    },
  },
  plugins: [],
};
