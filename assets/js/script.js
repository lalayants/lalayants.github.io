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
      console.log(this.innerHTML.toLowerCase())
      if (this.innerHTML.toLowerCase() === pages[i].dataset.page) {
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

// const blog_articles = document.querySelector("")
const contact_form_button = document.getElementById("contact_form_button");
contact_form_button.addEventListener('click', function() {
  const contact_form_name = document.querySelector("#contact_form_name").value;
  const contact_form_link = document.querySelector("#contact_form_link").value;
  const contact_form_text = document.querySelector("#contact_form_text").value;
  // console.log(contact_form_name, contact_form_link, contact_form_text);
  console.log(contact_form_name);
  console.log(contact_form_link);
  console.log(contact_form_text);
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
      console.log('done ajax');
      // window.alert("d");
    },
    error: function() {
      console.log('not done ajax');
      // window.alert("n d");
    }
  });
  setTimeout(1000);
  console.log('done listener');

});
