document.addEventListener("DOMContentLoaded", function() {
    var url = window.location.href;
    var lastPath = url.split('/');

    var lastPathElement = lastPath[lastPath.length - 2];
        console.log(lastPathElement)
        
        const peremen = document.getElementById("127.0.0.1:8000")
        const peremen1 = document.getElementById("loginadmin")
    
    if(lastPathElement == peremen.id){
        peremen.style.borderBottom= "2px solid rgba(4, 120, 87, 1)";
    }else if (lastPathElement == peremen1.id){
        peremen1.style.borderBottom= "2px solid rgba(4, 120, 87, 1)";
    }

});
