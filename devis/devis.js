let number = 0;

function addRow(){
  if (number % 2 == 0) {
    const textHTML = `
        <div class="yellow-section" class="js-section-${number}">
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <p>
                <!-- nothing -->
            </p>
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
    </div>
    `; 
    let gridDevisFacture = document.querySelector('.grid-devis-facture');
    gridDevisFacture.innerHTML += textHTML;

  } else if (number % 2 != 0) {
    const textHTML = `
      <div class="white-section" class="js-section-${number}">
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <p>
                <!-- nothing -->
            </p>
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
        <div class="row-devis">
            <input class="input-devis-facture" type="text">
        </div>
    </div>
    `; 
    let gridDevisFacture = document.querySelector('.grid-devis-facture');
    gridDevisFacture.innerHTML += textHTML;
  };

  number += 1;
};