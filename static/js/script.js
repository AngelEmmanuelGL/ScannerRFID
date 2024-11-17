function agregarNumero() {
  const numeroInput = document.getElementById("numero");
  const numero = numeroInput.value.trim();
  if (!numero || isNaN(numero)) {
      alert("Por favor, ingresa un número válido.");
      return;
  }

  fetch(`/consultar_alumno/?numero=${numero}`, {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
      },
  })
  .then(response => response.json())
  .then(data => {
    console.log("Respuesta del servidor:", data);
      if (data.error) {
          alert('Error: ' + data.error);
      } else {
          const tabla = document.getElementById("tablaNumeros").getElementsByTagName('tbody')[0];
          const nuevaFila = tabla.insertRow();

          const celdaNumero = nuevaFila.insertCell();
          celdaNumero.textContent = numero;

          const celdaNombre = nuevaFila.insertCell();
          celdaNombre.textContent = data.nombre;

          const celdaHora = nuevaFila.insertCell();
          celdaHora.textContent = data.hora;

          numeroInput.value = "";
          numeroInput.focus();
      }
  })
  .catch(error => {
      console.error('Error:', error);
      alert('Hubo un problema con la solicitud.');
  });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
