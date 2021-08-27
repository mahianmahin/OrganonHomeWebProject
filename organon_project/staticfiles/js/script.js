// if (window.outerWidth < 1024) {
//     document.getElementById('logo_img').src = "../img/logo/logo_main.png";
// };

document.getElementById('toggle_btn').addEventListener('click', () => {
    document.getElementById('phone_nav').style.right = 0;
    document.getElementById('overlay').style.display = "block";
});

document.getElementById('back').addEventListener('click', () => {
    document.getElementById('phone_nav').style.right = "-150%";
    document.getElementById('overlay').style.display = "none";
});