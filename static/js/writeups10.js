function changeImage() {

    if (document.getElementById("imgClickAndChange").src == "https://www.jing.fm/clipimg/full/132-1327227_moon-clipart-moon-clipart-black-and-white-half.png") {
        document.getElementById("imgClickAndChange").src = "https://www.jing.fm/clipimg/full/63-631481_rays-clipart-black-grey-sun-sun-cartoon-png.png";
        document.body.style.background = "#ffffff";
        document.body.style.color = "#37393e";
        var x = document.getElementsByClassName("chall");
        for (var i = 0; i < x.length; i++) {
            x[i].style.background = "#f3f3f4";
            x[i].style.color = "#37393e"
        }
        var x = document.getElementsByClassName("pre");
        for (var i = 0; i < x.length; i++) {
            x[i].style.background = "#f3f3f4";
            x[i].style.color = "#37393e";
        }
        var oldlink = document.getElementsByTagName("link").item(0);

        var newlink = document.createElement("link");
        newlink.setAttribute("rel", "stylesheet");
        newlink.setAttribute("type", "text/css");
        newlink.setAttribute("href", "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.7.2/build/styles/default.min.css");

        document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
    }
    else {
        document.getElementById("imgClickAndChange").src = "https://www.jing.fm/clipimg/full/132-1327227_moon-clipart-moon-clipart-black-and-white-half.png";
        document.body.style.background = "#37393e";
        document.body.style.color = "#ffffff";
        var x = document.getElementsByClassName("chall");
        for (var i = 0; i < x.length; i++) {
            x[i].style.background = "#2f3037";
            x[i].style.color = "#ffffff";
        }
        var x = document.getElementsByClassName("pre");
        for (var i = 0; i < x.length; i++) {
            x[i].style.background = "#1e1e1e";
            x[i].style.color = "#ffffff";
        }
        var oldlink = document.getElementsByTagName("link").item(0);

        var newlink = document.createElement("link");
        newlink.setAttribute("rel", "stylesheet");
        newlink.setAttribute("type", "text/css");
        newlink.setAttribute("href", "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.7.2/build/styles/an-old-hope.min.css");

        document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
    }
}
function showCode() {
    if (document.getElementById("icicle-beginner").style.display == "inline") {
        document.getElementById("icicle-beginner").style.display = "none";
    } else {
        document.getElementById("icicle-beginner").style.display = "inline";
    }
}