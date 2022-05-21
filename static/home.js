window.onload = () => {

    document.querySelectorAll('.scene').forEach((elem) => {
        const modifier = elem.getAttribute('data-modifier')
        basicScroll.create({
            elem: elem,
            from: 0,
            to: 519,
            direct: true,
            props: {
                '--translateY': {
                    from: '0',
                    to: `${ 10 * modifier }px`
                }
            }
        }).start()

    })





    var text="";
    const fullText1 = "Get maximum insights from a paragraph...";
    const fullText2 = "Summarize the long paragraphs to the short one ...";
    const fullText3 = "Auto generated mock test based on the paragraph...";
    const texts=[""];
    for (let i = 1; i <= fullText1.length; i++) {
        text=fullText1.slice(0,i);
        texts.push(text);
    }
    for (let i = 0; i < 10; i++) {
        texts.push(fullText1);
    }
    for (let i = fullText1.length; i >= 0; i=i-2) {
        text=fullText1.slice(0,i);
        texts.push(text);
    }
    for (let i = 1; i <= fullText2.length; i++) {
        text=fullText2.slice(0,i);
        texts.push(text);
    }
    for (let i = 0; i < 10; i++) {
        texts.push(fullText2);
    }
    for (let i = fullText2.length; i >= 0; i=i-2) {
        text=fullText2.slice(0,i);
        texts.push(text);
    }
    for (let i = 1; i <= fullText3.length; i++) {
        text=fullText3.slice(0,i);
        texts.push(text);
    }
    for (let i = 0; i < 10; i++) {
        texts.push(fullText3);
    }
    for (let i = fullText3.length; i >= 0; i=i-2) {
        text=fullText3.slice(0,i);
        texts.push(text);
    }



    var i=0,j=0, j2=0;
    const arrayLen = texts.length;
    function Screen() {
    setInterval(function () {
        if (i==arrayLen) {
            i=0;
        }
        text = texts[i++];
            document.getElementById("text").innerHTML=text;
    },100)
    setInterval(function(){
        if(j==0){
            document.getElementById("span").style.opacity=0;
        }
        if(j==1){
            document.getElementById("span").style.opacity=0.25;
        }
        if(j==2){
            document.getElementById("span").style.opacity=0.5;
        }
        if(j==3){
            document.getElementById("span").style.opacity=1;
        }
        if(j==4){
            document.getElementById("span").style.opacity=0.5;
        }
        if(j==5){
            document.getElementById("span").style.opacity=0.25;
        }
        if (j==6) {
            document.getElementById("span").style.opacity=0;
        }
        j++;
        if (j==7) {
            j=0;
        }
    },100);
    }

    setInterval(function(){
            document.getElementById("span-2").style.opacity=j2/150;
        j2++;
        if (j2==150) {
            j2=0;
        }
    },10);
    Screen();


}


// FOR LOADER

function loaded(){
    document.getElementById("loading").style.display = "none";
 }
