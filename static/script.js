document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const loadingOverlay = document.getElementById("loading-overlay");
  const fadeEls = document.querySelectorAll(".fade-in");

  if (form && loadingOverlay) {
    form.addEventListener("submit", () => {
      loadingOverlay.classList.remove("hidden");
    });
  }

  fadeEls.forEach((el) => {
    el.style.animationDelay = "0.1s";
    el.classList.add("fade-in");
  });
});
