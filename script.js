// let elementsLeft = document.querySelectorAll(`.left .element`)
// let elementsRight = document.querySelectorAll(`.right .element`)


// function rd(min,max){
//     return Math.random() * (max - min) + min;
// }

// elementsLeft.forEach(element => {
//     element.style.width = rd(45,60)+'%';
//     element.style.marginTop = rd(4,20)+"rem";
//     element.style.left = rd(2,10)+"rem";
// });


// elementsRight.forEach(element => {
//     element.style.width = rd(45,60)+'%';
//     element.style.marginTop = rd(4,20)+"rem";
//     element.style.left = rd(10,20)+"rem";
// });







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
            let titl = proj.appendChild(document.createElement('a'))
            // let pic = proj.querySelector('img').getAttribute('src')
            proj.querySelector('img').style.opacity = '0.5'
            // titl.style.backgroundImage = "url(" + pic +")"
            titl.href = proj.dataset.slug
            titl.innerHTML = proj.dataset.title
            titl.classList.add('overed')
        })

        proj.addEventListener("mouseleave", () => {
            proj.querySelector('img').style.opacity = '1'
            document.querySelector('.overed').remove()
        })

    });
    }

    var x = window.matchMedia("(max-width: 1050px)")

    if (!x.matches) { // If media query matches
        bo()

    } 

  




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
            document.querySelector("#fakeBackground").style.display = "block"
            document.querySelector("#toggle").innerHTML = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.29289 5.29289C5.68342 4.90237 6.31658 4.90237 6.70711 5.29289L12 10.5858L17.2929 5.29289C17.6834 4.90237 18.3166 4.90237 18.7071 5.29289C19.0976 5.68342 19.0976 6.31658 18.7071 6.70711L13.4142 12L18.7071 17.2929C19.0976 17.6834 19.0976 18.3166 18.7071 18.7071C18.3166 19.0976 17.6834 19.0976 17.2929 18.7071L12 13.4142L6.70711 18.7071C6.31658 19.0976 5.68342 19.0976 5.29289 18.7071C4.90237 18.3166 4.90237 17.6834 5.29289 17.2929L10.5858 12L5.29289 6.70711C4.90237 6.31658 4.90237 5.68342 5.29289 5.29289Z" /></svg>'
        } else { 
            document.querySelector(".burger").style.display = "none"
            document.querySelector("#fakeBackground").style.display = "none"
            document.querySelector("#toggle").innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 50 50"><path d="M 0 9 L 0 11 L 50 11 L 50 9 Z M 0 24 L 0 26 L 50 26 L 50 24 Z M 0 39 L 0 41 L 50 41 L 50 39 Z"></path></svg>'
        }
        toggle = !toggle
    
}

let toggle = true
document.querySelector("#toggle").addEventListener("click", ()=>{
   toggleMenu()
})

let egg =  document.getElementById("egg")
let toggleEgg = false

egg.addEventListener("click", ()=>{
        egg.style.zIndex = 100
        setTimeout(() => {
            toggleEgg = !toggleEgg
        }, 100);
  })

    document.body.addEventListener('click', ()=>{
        if (toggleEgg == true){
            egg.style.zIndex = -10
    }
    })
  


var swiper = new Swiper(".swiper", {
    loop: true,
    // autoplay: true,
    clickable: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },

      pagination: {
        el: ".swiper-pagination",
        dynamicBullets: true,
      },
  });




function openFriends(){
    document.querySelector("#friends").style.display = 'inline'
    // toggleMenu(false)
}
function closeFriends(){
    document.querySelector("#friends").style.display = 'none'
}

function lightingNews(){
    document.querySelector('footer').classList += 'animated'

    setTimeout(() => {
        document.querySelector('footer').classList.remove("animated")
    }, 1500);
}


// when window resize close the burger menu if it's opened
window.onresize = function(event) {
    if (document.querySelector(".burger").style.display = "flex"){
        document.querySelector(".burger").style.display = "none"
        document.querySelector("#fakeBackground").style.display = "none"
        document.querySelector("#toggle").innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 50 50"><path d="M 0 9 L 0 11 L 50 11 L 50 9 Z M 0 24 L 0 26 L 50 26 L 50 24 Z M 0 39 L 0 41 L 50 41 L 50 39 Z"></path></svg>'
    
    }
 
};



// if (x.matches) { // If media query matches
//     window.location.href = 'https://lorenzoponte.com'
// } 


// document.querySelectorAll('.marquee').forEach(marquee => {
//     if (x.matches) { // If media query matches
//     marquee.addEventListener('')
// } 
// });
