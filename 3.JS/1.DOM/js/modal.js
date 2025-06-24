const open = document.getElementById('open');
const close = document.getElementById('close');

// const modal = document.getElementsByClassName('modal-wrapper')[0];
const modal = document.querySelector('.modal-wrapper'); // 더 이쁨

// open.onclick = function openmodal() {}
// open.onclick = function () {}
open.onclick = () => {
    showModal();
}

// close.onclick = () => {
//     modal.style.display = 'none';
// }

function showModal() {
    const modalWrapper = document.createElement('div');
    modalWrapper.className = 'modal-wrapper';
    modalWrapper.style.display = 'flex';

    modalWrapper.innerHTML = `
        <div class="modal">
            <div class="modal-title">모달 타이틀</div>
            <p>본문 내용 Lorem ipsum, dolor sit amet consectetur adipisicing elit. Adipisci tempora dolores nemo sint
                voluptas, est veniam incidunt, molestiae voluptates debitis, iste omnis? Ad aut labore eius illo,
                dolores accusamus ea.</p>
            <div class="close-wrapper">
                <button id="close">닫기</button>
            </div>
        </div>
        `

    document.body.appendChild(modalWrapper);

    document.getElementById('close').onclick = () => {
        modalWrapper.remove();
    }
}