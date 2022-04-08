const navSlide = () => {
    const dropdown = document.querySelector('.dropdown');
    const NavBar = document.querySelector ('.Nav');
    const Nav = document.querySelectorAll('.Nav li');

    //Show Small Navigation Bar
    dropdown.addEventListener('click', ()=>{
        NavBar.classList.toggle('Nav-active');
    
    //Animate Nav Li
        Nav.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            }
            else {
                link.style.animation = `NavFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
    });
}

navSlide();