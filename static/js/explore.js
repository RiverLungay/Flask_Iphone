const image = document.getElementById("product-image");
const magnifier = document.getElementById("magnifier");
const zoomed = document.getElementById("magnified-image");

image.addEventListener("mousemove", function (e) {
  const rect = image.getBoundingClientRect();
  const x = e.clientX - rect.left; // x position within the image
  const y = e.clientY - rect.top; // y position within the image

  // Show magnifier
  magnifier.style.display = "block";
  magnifier.style.left = e.pageX + 20 + "px"; // offset to right of cursor
  magnifier.style.top = e.pageY - 60 + "px"; // slightly above cursor

  // Calculate zoom position
  const percentX = x / rect.width;
  const percentY = y / rect.height;

  // Move zoomed image inside magnifier (with scaling)
  zoomed.style.left = `-${
    percentX * zoomed.offsetWidth - magnifier.offsetWidth / 2
  }px`;
  zoomed.style.top = `-${
    percentY * zoomed.offsetHeight - magnifier.offsetHeight / 2
  }px`;
});

image.addEventListener("mouseleave", function () {
  magnifier.style.display = "none";
});
