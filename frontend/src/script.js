const button = document.getElementById("message-button");
const message = document.getElementById("message");
const themeButton = document.getElementById("theme-button");
const themeStatus = document.getElementById("theme-status");

const themeDescriptions = {
  light: "You are viewing the light theme: dark text on a bright background.",
  dark: "You are viewing the dark theme: light text on a dark background, easier on the eyes in a dim room."
};

const messages = [
  "Welcome to the workshop! 👋",
  "Nice click! Small changes add up.",
  "Thanks for stopping by. Have fun today!"
];

let index = 0;

button.addEventListener("click", () => {
  message.textContent = messages[index];
  index = (index + 1) % messages.length;

  // Restart the fade-in animation on every click.
  message.classList.remove("is-visible");
  void message.offsetWidth;
  message.classList.add("is-visible");
});

themeButton.addEventListener("click", () => {
  const isDark = document.documentElement.dataset.theme === "dark";
  const nextTheme = isDark ? "light" : "dark";

  document.documentElement.dataset.theme = nextTheme;
  themeButton.setAttribute("aria-pressed", String(nextTheme === "dark"));
  themeButton.textContent =
    nextTheme === "dark" ? "Switch to light theme" : "Switch to dark theme";
  themeStatus.textContent = themeDescriptions[nextTheme];
});

const infoWorkshop = document.getElementById("info-workshop");
const infoPython = document.getElementById("info-python");

async function loadWorkshopVersionInfo() {
  try {
    const response = await fetch("/api/workshop-version-info");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const info = await response.json();
    infoWorkshop.textContent = info.workshop;
    infoPython.textContent = info.python_version;
  } catch (error) {
    infoWorkshop.textContent = "Not available right now";
    infoPython.textContent = "Not available right now";
  }
}

loadWorkshopInfo();
