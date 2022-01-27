const header = document.getElementById("header");
const formContainer = document.getElementById("form-container");
const inpFile = formContainer.querySelector(".file");
const imagePreview = formContainer.querySelector(".image-preview");
const image = imagePreview.querySelector(".image-preview--image");
const text = imagePreview.querySelector(".image-preview--text");
const submit = formContainer.querySelector(".submit");
const upload = formContainer.querySelector("#upload");
const dateEl = document.getElementById('date')

currentDate = new Date()
dateEl.textContent = currentDate.getFullYear()

console.log('working...');

const file = null;
if (!file) {
    submit.style.display = "none";
    formContainer.style.height = "70vh";
}

//file upload
inpFile.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();
        text.style.display = "none";
        image.style.display = "block";
        submit.style.display = "";
        upload.style.display = "none"
        formContainer.style.height = "90vh";
        formContainer.style.marginBottom = "3rem";

        reader.addEventListener("load", function () {
            image.setAttribute("src", this.result);
            image.style.width = "100%";
        });

        reader.readAsDataURL(file);
    }
});

//stcky header
window.onscroll = function () {
    scroll();
};
let sticky = header.offsetTop;
function scroll() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}
