
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

let projs = document.querySelectorAll('.element')

projs.forEach(proj => {
    proj.addEventListener("mouseenter", () => {
        let titl = proj.appendChild(document.createElement('h1'))
        let pic = proj.querySelector('img').getAttribute('src')
        titl.style.backgroundImage = "url(" + pic +")"
        titl.innerHTML = proj.dataset.title
    })

    proj.addEventListener("mouseleave", () => {
        document.querySelector('.element h1').remove()
    })

});