const floatingPet = document.querySelector(".floating-pet");
let phase = 0;

function animateFloatingPet() {
  phase += 0.02;
  if (floatingPet) {
    floatingPet.style.transform = `translateY(${Math.sin(phase) * 18}px)`;
  }
  window.requestAnimationFrame(animateFloatingPet);
}

animateFloatingPet();
