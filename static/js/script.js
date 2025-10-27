document.getElementById("btnCita").addEventListener("click", async () => {
    const respuesta = await fetch("/cita");
    const data = await respuesta.json();
    document.getElementById("cita").textContent = data.cita;
});
