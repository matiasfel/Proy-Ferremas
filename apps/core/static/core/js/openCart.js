function openCart(){
    let cart = document.getElementById('cart');
    if (cart) {
        cart.classList.toggle('open');
        if (cart.classList.contains('open')) {
            cart.style.display = 'block';
        } else {
            cart.style.display = 'none';
        }
    }
}