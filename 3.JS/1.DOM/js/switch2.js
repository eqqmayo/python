// css 분리했듯 독립적으로, 인라인 style 잘 안 쓰듯이
// js도 인라인 js인 onclick, onxxxx 이런것들 권장하지 않음

document.addEventListener('DomContentLoaded', function() {
    // 여기는 브라우저가 DOM을 다 불러왔을때 호출됨
    let fruitSelector = document.getElementById('fruitSelector');
    fruitSelector.addEventListener('change', function() {

    });

});

function fruitDisplay() {
    let fruit = document.getElementById('fruitSelector').value;
    let result = document.getElementById('result');
    // if (fruit === 'apple') {
    //     result.innerText = '이것은 사과입니다';
    // } else if (fruit === 'banana') {
    //     result.innerText = '이것은 바나나입니다';
    // } 

    // 이 switch/case 는 언제나 if/else 로 대체 가능
    // 가독성 좋게 하기위해 생긴 문법
    // case 가 끝났을때 break 없으면 아래 코드 다 처리 - break 생긴 배경은 여러 케이스를 같이 처리하기위함
    switch (fruit) {
        case 'apple':
        case 'APPLE':
            result.innerText = '이것은 사과입니다';
            break;
        case 'banana':
            result.innerText = '이것은 바나나입니다';
            break;
        case 'orange':
            result.innerHTML = '이것은 오렌지입니다';
            break;
        case 'pineapple':
            result.innerHTML = '<b>이것은 파인애플입니다</b>';
            break;
        default:
            result.textContent = '과일 먹고싶다';
    }
}