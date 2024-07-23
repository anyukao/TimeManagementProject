document.addEventListener("DOMContentLoaded", function() {
    var url = window.location.href;
    var lastPath = url.split('/');

    var lastPathElement = lastPath[lastPath.length - 2];
        console.log(lastPathElement)

    const peremen = document.getElementById("udalennyesotrudniki")
    const peremen1 = document.getElementById("uchetvremeni")
    const peremen2 = document.getElementById("adminpage")
   
   if(lastPathElement==peremen.id){
    peremen.style.borderBottom= "2px solid rgba(4, 120, 87, 1)";
   }else if(lastPathElement == peremen1.id){
    peremen1.style.borderBottom= "2px solid rgba(4, 120, 87, 1)";
   }else if(lastPathElement == peremen2.id){
    peremen2.style.borderBottom= "2px solid rgba(4, 120, 87, 1)";
   }
   
   
    // console.log(peremen)
   
  });

