const choiceBlocks = document.getElementsByClassName('choice_block')
const confirmBtn = document.getElementById('confirmbtn')
const answerZone = document.getElementById('answerZone')


var selectedBlock


for (let index = 0; index < choiceBlocks.length; index++) {
    choiceBlocks[index].addEventListener('click', selectOne)
}

confirmBtn.addEventListener('click', postQuestion);


function selectOne(e) {
    // 获取外层的choice_block元素
    block = e.target
    while (!block.classList.contains('choice_block')) {
        block = block.parentNode
    }
    selectedBlock = block
    currentSingleChoiceNo = block.getAttribute('scno')
    // 二次点击取消选中状态
    if (block.classList.contains('selected')) {
        block.classList.remove('selected')
        return
    }
    // 点击并选中其他block
    choises = document.getElementsByClassName('choice_block')
    for (let index = 0; index < choises.length; index++) {
        choises[index].classList.remove('selected')
    }
    block.classList.add('selected')
}


function postQuestion() {
    if (!selectedBlock) {
        sweetAlert('info', '请先选择一个选项！')
        return;
    }
    if (confirmBtn.getAttribute('clicked')) {
        sweetAlert('info', '次题已刷,请选择下一题')
        return;
    }

    let selectedNo = selectedBlock.getAttribute('scno');
    let selectedChoice = selectedBlock.getAttribute('choice');
    let rightChoice = selectedBlock.getAttribute('rsc')
    if (selectedChoice === rightChoice) {
        selectedBlock.classList.add('success');
    } else {
        selectedBlock.classList.add('failed');
    }
    answerZone.style.display = 'block';
    confirmBtn.setAttribute('clicked', true)
    // confirmBtn.setAttribute('disabled', true)
    
    fetch("/exercise/single-choice", {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'choice': selectedChoice,
            'sc-no': selectedNo,
        }
    })
}
