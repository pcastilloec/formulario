document.getElementById('sistema').addEventListener('change', function() {
    var sistema = this.value;
    var camposSistemaNH3 = document.getElementById('campos-sistema-nh3');

    if (sistema === 'SISTEMA_NH3') {
        camposSistemaNH3.style.display = 'block';
    } else {
        camposSistemaNH3.style.display = 'none';
    }
});