$(document).ready(
    function() {
        const loading = document.querySelector('.loading');

        loading.style.display = 'none'
    }
);

function loadPage() {
    const loading = document.querySelector('.loading');
    const loadBox = document.querySelector('.loaddingBlock');

    loadBox.style.display = 'block'
    loading.style.display = 'flex'
}


