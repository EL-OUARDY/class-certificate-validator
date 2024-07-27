document.addEventListener('DOMContentLoaded', function () {

  const button = document.getElementById("checkBtn");
  button.addEventListener('click', function () {
    const code = document.getElementById("certificate-code").value

    if (code) {
      const url = `/certificate/${code}`
      window.location.href = url;
    }
  });
});
