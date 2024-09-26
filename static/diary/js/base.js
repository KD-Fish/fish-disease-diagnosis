// static/diary/js/base.js

function updateDateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hour = String(now.getHours()).padStart(2, '0');
    const minute = String(now.getMinutes()).padStart(2, '0');
    const second = String(now.getSeconds()).padStart(2, '0');

    const formattedDateTime = `${year}年${month}月${day}日${hour}時${minute}分${second}秒`;

    document.getElementById('datetime').textContent = formattedDateTime;
}

// 初回実行
updateDateTime();

// 1秒ごとに更新
setInterval(updateDateTime, 1000);
