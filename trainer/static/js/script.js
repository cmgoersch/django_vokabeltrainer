document.addEventListener('DOMContentLoaded', function () {
    const addButton = document.querySelector('a');

    // Prüfen, ob der Benutzer das Pop-up bereits gesehen hat
    if (!localStorage.getItem('alertShown')) {
        addButton.addEventListener('click', function (event) {
            alert('Du wirst nun ein neues Wort hinzufügen!');
            localStorage.setItem('alertShown', 'true');  // Speichern, dass das Pop-up bereits gezeigt wurde
        });
    }
});