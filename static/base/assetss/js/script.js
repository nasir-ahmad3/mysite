let nav = document.querySelector('body > nav')

window.addEventListener('scroll', e => {
	if (window.scrollY != 0 && window.scrollY > 0){
		nav.classList.add('stiky')
	}else{
		nav.classList.remove('stiky')
	}

})
// responsive nav bar 
let btn = document.querySelector('.button-menu')

btn.addEventListener('click', e => {
	nav.classList.toggle('active')
})



let cards = document.querySelectorAll('.card-wrapper > .card')

Array.from(cards).forEach(card => {
	card.addEventListener('mouseover', e => {
		Array.from(cards).forEach(c => {
			c.classList.remove('active')
			c.classList.add('deactive')
		})
		card.classList.remove('deactive')
		card.classList.add('active')
	})
	card.addEventListener('mouseleave', e => {
		Array.from(cards).forEach(c => {
			c.classList.remove('active')
			c.classList.remove('deactive')
		})
	})
})

