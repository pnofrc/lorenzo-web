let elementsLeft = document.querySelectorAll(`.left .element`)
let elementsRight = document.querySelectorAll(`.right .element`)


function rd(min,max){
    return Math.random() * (max - min) + min;
}

elementsLeft.forEach(element => {
    element.style.width = rd(45,60)+'%';
    element.style.marginTop = rd(4,20)+"rem";
    element.style.left = rd(2,10)+"rem";
});


elementsRight.forEach(element => {
    element.style.width = rd(45,60)+'%';
    element.style.marginTop = rd(4,20)+"rem";
    element.style.left = rd(10,20)+"rem";
});


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





// DA TENERE

//     let opening_pics = ['_DSC7702.JPG','Buoni_a_nulla.JPG','Ido.jpg','Ido2.jpg','Sito.JPG'] 

// let i = 0;
// let x;
// let y;

// function addPic(event) {

//         x = event.clientX;
//         y =  event.clientY;
//         r = Math.floor(Math.random() * (10 - (-10)) +  (-10))

//         document.querySelector(".presentazione").innerHTML+=`<img class="opening-pic" style="top:${y}px; left:${x}px; transform: rotate(${r}deg)" src="apertura/${opening_pics[i]}">`
//         i++
//         if (i >= opening_pics.length){
//             i = 0
//         }
//     }

// document.querySelector(".presentazione").addEventListener("click", addPic)




function toggleMenu(tog){
    
        if (toggle){
            document.querySelector(".burger").style.display = "flex"
            document.querySelector("#toggle").innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 50 50">        <path d="M 7.71875 6.28125 L 6.28125 7.71875 L 23.5625 25 L 6.28125 42.28125 L 7.71875 43.71875 L 25 26.4375 L 42.28125 43.71875 L 43.71875 42.28125 L 26.4375 25 L 43.71875 7.71875 L 42.28125 6.28125 L 25 23.5625 Z"></path></svg>'
        } else { 
            document.querySelector(".burger").style.display = "none"
            document.querySelector("#toggle").innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 50 50"><path d="M 0 9 L 0 11 L 50 11 L 50 9 Z M 0 24 L 0 26 L 50 26 L 50 24 Z M 0 39 L 0 41 L 50 41 L 50 39 Z"></path></svg>'
        }
        toggle = !toggle
    
}

let toggle = true
document.querySelector("#toggle").addEventListener("click", (toggle)=>{
   toggleMenu()
})



var swiper = new Swiper(".swiper", {
    loop: true,
    clickable: true,
    // autoplay: {
    //     delay: 2500,
    //     disableOnInteraction: false,
    //   },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },

      pagination: {
        el: ".swiper-pagination",
        dynamicBullets: true,
      },
  });