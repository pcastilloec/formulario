document.addEventListener('DOMContentLoaded', function() {
    const rcksSelect = document.querySelector('select[name="RCKS"]');
    const extraFields = [
        'PRESION_BAJA_PSIG',
        'CORRIENTE',
        'VOLTAJE',
        'ESTADO_DEL_CONDENSADOR',
        'NIVEL_DE_REFRIGERANTE',
        'PRESION_ALTA_PSIG'
    ];

    const rcksWithExtraFields = [
        "ICESTA 1", "ICESTA 2", "ICESTA 3", "ICESTA 4", "ICESTA 5",
        "ICESTA 6", "ICESTA 7", "ICESTA 8", "ICESTA 9", "RACK 10",
        "RACK 11", "RACK 12", "RACK 13", "ICESTA 14", "RACK 15",
        "RACK 16", "RACK 17", "ICESTA 18", "ICESTA 19", "ICESTA 20",
        "HOWES 1", "HOWES 2", "HOWES 3", "SISTEMA NH3"
    ];

    function toggleExtraFields() {
        const selectedValue = rcksSelect.value;
        const shouldShow = selectedValue === 'SISTEMA NH3' || rcksWithExtraFields.includes(selectedValue);

        extraFields.forEach(fieldName => {
            const field = document.querySelector(`[name="${fieldName}"]`);
            if (field) {
                const fieldContainer = field.closest('.form-group') || field.parentElement;
                if (shouldShow) {
                    field.style.display = 'block';
                    fieldContainer.style.display = 'block';
                } else {
                    field.style.display = 'none';
                    fieldContainer.style.display = 'none';
                }
            }
        });
    }
       if (rcksSelect) {
        toggleExtraFields();
        rcksSelect.addEventListener('change', toggleExtraFields);
    }
});

document.getElementById('sistema').addEventListener('change', function() {
    var sistema = this.value;
    var camposNH3 = document.getElementById('campos-nh3');
    var camposSistemaNH3 = document.getElementById('campos-sistema-nh3');
  
    if (sistema === 'NH3') {
      camposNH3.style.display = 'block';
      camposSistemaNH3.style.display = 'none';
    } else if (sistema === 'SISTEMA_NH3') {
      camposNH3.style.display = 'none';
      camposSistemaNH3.style.display = 'block';
    } else {
      camposNH3.style.display = 'none';
      camposSistemaNH3.style.display = 'none';
    }
  });