const pet = document.querySelector(".pet-button");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
let frameId = 0;
let phase = 0;

function renderPet() {
  if (!pet || reduceMotion.matches) {
    frameId = 0;
    return;
  }

  phase += 0.015;
  pet.style.transform = `translateY(${Math.sin(phase) * 3}px)`;
  frameId = window.requestAnimationFrame(renderPet);
}

function syncMotionPreference() {
  if (!pet) {
    return;
  }

  if (reduceMotion.matches) {
    if (frameId) {
      window.cancelAnimationFrame(frameId);
      frameId = 0;
    }
    pet.style.transform = "none";
    return;
  }

  if (!frameId) {
    frameId = window.requestAnimationFrame(renderPet);
  }
}

pet?.addEventListener("click", () => {
  const pressed = pet.getAttribute("aria-pressed") === "true";
  pet.setAttribute("aria-pressed", String(!pressed));
});

reduceMotion.addEventListener("change", syncMotionPreference);
syncMotionPreference();
