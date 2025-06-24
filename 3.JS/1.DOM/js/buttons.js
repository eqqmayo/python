function increase() {
    let number = document.getElementById('result'); 
    // div 요소 안에 있는 글을 가져오는 3가지 방식
    // - innerText: 글자만 (디자인 속성 적용 받음)
    // - innerHTML: 글자 + 태그 (디자인 속성 적용 안 받음)
    // - textContent: 순수 글자만 (디자인 속성 적용 안 받음)
    let result = number.textContent;
    result = parseInt(result) + 1;
    number.textContent = result;
}

function decrease() {
    let number = document.getElementById('result'); 
    let number_string = number.textContent;

    // let number_string_to_number = Number(number_string);
    let result = number_string - 1;
    number.textContent = result;
}

function decrease_final() {
    document.getElementById('result').textContent -= 1;
}