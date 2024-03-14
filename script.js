
function eraseCategories(){

    let cat = document.querySelectorAll(`.element`)
    cat.forEach(cat_element => {
        cat_element.style.display = "none"
    });

}

function selectCategory(category){

    eraseCategories()

   
    if (category == 'all'){
        let cat = document.querySelectorAll(`.element`)

        cat.forEach(cat_element => {
            cat_element.style.display = "block"
        });
    } else {
        let cat = document.querySelectorAll(`.${category}`)

        cat.forEach(cat_element => {
            cat_element.style.display = "block"
        });
    }


}

