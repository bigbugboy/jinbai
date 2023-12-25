const telephoneField = document.getElementById('telephone')
const verifycodeField = document.getElementById('code')
const sendcodebtn = document.getElementById('sendcodebtn')
const postBtn = document.getElementById('postBtn')


// 如下方法来自 common.js
// sweetAlert, getCookie


// 倒计时
function startCountdown(seconds) {
    sendcodebtn.innerHTML = seconds + "s";
    
    var countdownInterval = setInterval(function() {
      seconds--;
      sendcodebtn.innerHTML = seconds + "s";
  
      if (seconds <= 0) {
        clearInterval(countdownInterval);
        sendcodebtn.innerHTML = "";
        // 启用按钮
        sendcodebtn.innerHTML = "重新发送";
        sendcodebtn.removeAttribute('disabled')
      }
    }, 1000);
}


sendcodebtn.addEventListener('click', () => {
    if (sendcodebtn.getAttribute('disabled')) {
        return
    }
    fetch("/user/send-verify-code", {
        method: 'POST',
        headers: {
            Accept: 'application.json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'telephone': telephoneField.value,
        }
    }).then((res) => res.json()).then((data) => {
        if (data.status === 'success') {
            // 请求成功，开始倒计时
            sendcodebtn.setAttribute('disabled', true)
            startCountdown(60);
        } else {
            sweetAlert('error', data.msg);
        }
    })

})


postBtn.addEventListener('click', (e) => {
    const telephone = telephoneField.value;
    const verifycode = verifycodeField.value;
    if (!telephone || !verifycode){
        e.preventDefault();
        sweetAlert('error', '手机号和验证码不能为空')
        return;
    }
    if (!sendcodebtn.hasAttribute('disabled')) {
        e.preventDefault();
        sweetAlert('error', '请先获取验证码')
        return;
    }
})