function changeImage() {
    if (document.getElementById("imgClickAndChange").src == "https://lh3.googleusercontent.com/proxy/vZ5VEiQxnZmYiBV0jPiORZabPamGLVQvduarZBiPOwCJB6hmE2fWnsoi6yIRhuyJDqbgHca-Np4tbEZh8_Sx-cIUAlkEfHEciJBPSiUOw2KTdvhS6gjSVcw") 
    {
        document.getElementById("imgClickAndChange").src = "https://www.freeiconspng.com/thumbs/heart-png/heart-png-15.png";
        document.cookie = "likes=\"{\"like\":1}\""; 
    }
    else 
    { 
        document.getElementById("imgClickAndChange").src = "https://lh3.googleusercontent.com/proxy/vZ5VEiQxnZmYiBV0jPiORZabPamGLVQvduarZBiPOwCJB6hmE2fWnsoi6yIRhuyJDqbgHca-Np4tbEZh8_Sx-cIUAlkEfHEciJBPSiUOw2KTdvhS6gjSVcw";
        document.cookie = "likes=\"{\"like\":0}\""; 
    }
}

function correctLike() {
  if (isLiked == 0) {
    document.getElementById("imgClickAndChange").src = "https://lh3.googleusercontent.com/proxy/vZ5VEiQxnZmYiBV0jPiORZabPamGLVQvduarZBiPOwCJB6hmE2fWnsoi6yIRhuyJDqbgHca-Np4tbEZh8_Sx-cIUAlkEfHEciJBPSiUOw2KTdvhS6gjSVcw"
  } else {
    document.getElementById("imgClickAndChange").src = "https://www.freeiconspng.com/thumbs/heart-png/heart-png-15.png";
  }
}

window.onload = function() {
  correctLike();
};