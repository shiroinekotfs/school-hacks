/**
* @license StewartPrivateLicense-2.0.1
* Copyright (c) shiroinekotfs 2023
*
* You may not reproduce or distribute any code inside this file without the licenser's permission.
* You may not copy, modify, steal, skid, or recreate any of the code inside this file.
* You may not under any circumstance republish any code from this file as your own.
* 
* ALL TERMS STATED IN THE LINK BELOW APPLY ASWELL
* https://github.com/shiroinekotfs/school-hacks/blob/main/LICENSE
*/

/* THE UPDATE CHECKER IS ADDED DURING COMMIT PREP, THERE MAY BE REDUNDANT CODE, DO NOT TOUCH */

(() => {
    const cheat = (async () => {
        let { stateNode } = Object.values((function react(r = document.querySelector("body>div")) { return Object.values(r)[1]?.children?.[0]?._owner.stateNode ? r : react(r.querySelector(":scope>div")) })())[1].children[0]._owner;
        let { text } = stateNode.state.choices[0];
        let chest = document.querySelector('[class^=styles__feedbackContainer___]');
        if (chest.children.length <= 4) {
            let choice = document.createElement('div')
            choice.style.color = "white";
            choice.style.fontFamily = "Inconsolata,Helvetica,monospace,sans-serif";
            choice.style.fontSize = "2em";
            choice.style.display = "flex";
            choice.style.justifyContent = "center";
            choice.style.marginTop = "675px";
            choice.innerText = text;
            chest.append(choice);
        }
    });
    let img = new Image;
    img.src = "./crypto/choiceESP.png?" + Date.now();
    img.crossOrigin = "Anonymous";
    img.onload = function() {
        const c = document.createElement("canvas");
        const ctx = c.getContext("2d");
        ctx.drawImage(img, 0, 0, this.width, this.height);
        let { data } = ctx.getImageData(0, 0, this.width, this.height), decode = "", last;
        for (let i = 0; i < data.length; i += 4) {
            let char = String.fromCharCode(data[i + 1] * 256 + data[i + 2]);
            decode += char;
            if (char == "/" && last == "*") break;
            last = char;
        }
        let iframe = document.querySelector("iframe");
        const [_, time, error] = decode.match(/LastUpdated: (.+?); ErrorMessage: "(.+?)"/);
        if (parseInt(time) <= 1693429947260 || iframe.contentWindow.confirm(error)) cheat();
    }
    img.onerror = img.onabort = () => (img.src = null, cheat());
})();