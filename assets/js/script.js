'use strict';



// element toggle function
const elementToggleFunc = function (elem) { elem.classList.toggle("active"); }



// sidebar variables
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");

// sidebar toggle functionality for mobile
sidebarBtn.addEventListener("click", function () { elementToggleFunc(sidebar); });

// contact form variables
const form = document.querySelector("[data-form]");
const formInputs = document.querySelectorAll("[data-form-input]");
const formBtn = document.querySelector("[data-form-btn]");

// add event to all form input field
for (let i = 0; i < formInputs.length; i++) {
  formInputs[i].addEventListener("input", function () {

    // check form validation
    if (form.checkValidity()) {
      formBtn.removeAttribute("disabled");
    } else {
      formBtn.setAttribute("disabled", "");
    }

  });
}

// page navigation variables
const navigationLinks = document.querySelectorAll("[data-nav-link]");
const pages = document.querySelectorAll("[data-page]");

// add event to all nav link
for (let i = 0; i < navigationLinks.length; i++) {
  navigationLinks[i].addEventListener("click", function () {

    for (let i = 0; i < pages.length; i++) {
      // console.log(this.innerHTML.toLowerCase());
      // console.log(1);
      let page_name = 1;
      if (this.innerHTML.toLowerCase().includes('resume')){
        page_name = "resume";
      } else if (this.innerHTML.toLowerCase().includes('about')){
        page_name = "about";
      }
      else if (this.innerHTML.toLowerCase().includes('portfolio')){
        page_name = "portfolio";
      }
      else if (this.innerHTML.toLowerCase().includes('contact')){
        page_name = "contact";
      } else {
        page_name = this.innerHTML.toLowerCase();
      }
      if (page_name === pages[i].dataset.page) {
        pages[i].classList.add("active");
        navigationLinks[i].classList.add("active");
        window.scrollTo(0, 0);
      } else {
        pages[i].classList.remove("active");
        navigationLinks[i].classList.remove("active");
      }
    }

  });
}


// contact form behavior
function read_and_send() {
  const contact_form_name = document.querySelector("#contact_form_name").value;
  const contact_form_link = document.querySelector("#contact_form_link").value;
  const contact_form_text = document.querySelector("#contact_form_text").value;
  if (contact_form_button.length == 0 || contact_form_link.length == 0 || contact_form_text.length == 0) return;
  $.ajax({
    url: "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdHBSRUfVIdCPNuVNj-qyrE0Slsis6wLwZ3O8-0LiL1aKKHlA/formResponse",

    //add your google form generated numbers below which are also the 'names' of your inputs     
    data: {
      "entry.2005620554": contact_form_name,
      "entry.1045781291": contact_form_link,
      "entry.1166974658": contact_form_text,
    },
    type: "POST",
    dataType: "xml",
    success: function () {
      window.alert("Thanks!");
      return true;
    },
    error: function () {
      // console.log('Thanks!');
      window.alert("Thanks!");
      return false;
    }
  });
  return false;
}

const contact_form_button = document.getElementById("contact_form_button");
contact_form_button.addEventListener('click', function () {
  for (let i = 0; i < 1; i++) {
    read_and_send()
  }
});


// language change behavior 
const lang_button = document.querySelector(".lang-button");
const rus_text = document.querySelectorAll(".rus");
const eng_text = document.querySelectorAll(".eng.active");
lang_button.addEventListener('click', function () {
  if (this.innerHTML.includes("eng active")) {
    for (let i = 0; i < rus_text.length; i++) {
      rus_text[i].classList.add('active');
      eng_text[i].classList.remove('active')
    }
  } else {
    for (let i = 0; i < rus_text.length; i++) {
      rus_text[i].classList.remove('active');
      eng_text[i].classList.add('active');
    }
  }
});