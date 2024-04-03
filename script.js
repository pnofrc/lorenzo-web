
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
            cat_element.style.display = "flex"
        });
    } else {
        let cat = document.querySelectorAll(`.${category}`)

        cat.forEach(cat_element => {
            cat_element.style.display = "flex"
        });
    }

    bo()

}

function bo(){

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
    }

    bo()


    let opening_pics = ['_DSC7702.JPG','Buoni_a_nulla.JPG','Ido.jpg','Ido2.jpg','Sito.JPG'] 

let i = 0;
let x;
let y;

function addPic(event) {
        x = event.clientX;
        y =  event.clientY;

        document.querySelector(".presentazione").innerHTML+=`<img class="opening-pic" style="top:${y}px; left:${x}px" src="apertura/${opening_pics[i]}">`
        i++
    }





document.querySelector(".presentazione").addEventListener("click", addPic)
