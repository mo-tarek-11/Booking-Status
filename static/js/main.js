  let progress = document.getElementById('progress');
  let totalHeaight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function()
  {
      let proogresHeight = (window.pageYOffset / totalHeaight)*100;
      progress.style.height = proogresHeight + "%";
  
  }









var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";  
  let progress = document.getElementById('progress');
  let totalHeaight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function()
  {
      let proogresHeight = (window.pageYOffset / totalHeaight)*100;
      progress.style.height = proogresHeight + "%";
  
  }
}  


// let vedio = document.querySelector('video');
let vedio = document.getElementsByClassName('v');
window.addEventListener('scroll' , function()
{
    let val = 1.5 + window.scrollY/-1000;
    vedio.style.opacity = val;
})  


let vedio2 = document.getElementById('svedio');
window.addEventListener('scroll' , function()
{
    let val2 = 1 + window.scrollY/-600;
    vedio2.style.opacity = val2;
})  
