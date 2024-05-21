

let modal = document.querySelector("#modal")
let closemodal = document.querySelector("#closemodal")


function openModal(){
    // modal.style.display = "block"
   modal.style.display = 'flex'
   document.querySelector(".corpus").style.overflow = 'hidden'
}

closemodal.addEventListener("click", ()=>{
        modal.style.display = 'none'

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

    //   pagination: {
    //     el: ".swiper-pagination",
    //     dynamicBullets: true,
    //   },
  });
