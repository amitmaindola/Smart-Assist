window.onload = () => {
    const showHideBtn = document.getElementById("showListBtn");
    const showHideList = document.getElementById("showList");

    var show = false;

    showHideBtn.addEventListener('click', ()=>{
        if(show){
            showHideList.style.display="none";
        }else{
            showHideList.style.display="block";
            showHideList.style.width="650px";
            showHideList.style.transform="translateX(200px)";
        }
        show=show^true;
        setTimeout(() => {
            showHideList.style.opacity=show;
            showHideList.style.transform="translateX(0px)";
        }, 300);
    })


    const text = document.getElementById("text");
    var textShow="Write the text here to get the useful insights...";
    var texts = [""];
    for (let index = 0; index < textShow.length+4; index++) {
        texts.push(textShow.slice(0, index));
    }
    // for (let index = 0; index <= textShow.length; index++) {
    //     texts.push(textShow.slice(0, textShow.length-index));
    // }

    var finalLen = texts.length;
    var j=0;
    var refreshId = setInterval(function() {
        text.innerText=texts[j];
        if (j == finalLen-1) {
          clearInterval(refreshId);
        }
        j++;
      }, 200);
}