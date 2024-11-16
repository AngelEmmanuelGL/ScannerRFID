function agregarNumero() {
    const numeroInput = document.getElementById("numero");
    const numero = numeroInput.value;
    const tabla = document.getElementById("tablaNumeros");
    const nuevaFila = tabla.insertRow();
  
    const celdaNumero = nuevaFila.insertCell();
    celdaNumero.textContent = numero;
  
    const celdaTiempo = nuevaFila.insertCell();
    celdaTiempo.textContent = tiempo;
  
    numeroInput.value = "";
  }

