// House Price Prediction — result plaque count-up animation
document.addEventListener("DOMContentLoaded", function () {
  var resultValue = document.querySelector(".result-value");
  if (!resultValue) return;

  var target = parseFloat(resultValue.getAttribute("data-value"));
  if (isNaN(target)) return;

  var duration = 1100; // ms
  var start = null;

  function formatRupees(n) {
    return "\u20B9 " + Math.round(n).toLocaleString("en-IN");
  }

  function step(timestamp) {
    if (!start) start = timestamp;
    var progress = Math.min((timestamp - start) / duration, 1);
    // ease-out cubic
    var eased = 1 - Math.pow(1 - progress, 3);
    resultValue.textContent = formatRupees(target * eased);

    if (progress < 1) {
      window.requestAnimationFrame(step);
    } else {
      resultValue.textContent = formatRupees(target);
    }
  }

  window.requestAnimationFrame(step);
});
