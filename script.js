
function eraseCategories(){

    let cat = document.querySelectorAll(`.element`)
    cat.forEach(cat_element => {
        cat_element.style.display = "none"
    });

}

function selectCategory(category){

    eraseCategories()

    let cat = document.querySelectorAll(`.${category}`)
    console.log(cat)
    cat.forEach(cat_element => {
        cat_element.style.display = "block"
    });
}

