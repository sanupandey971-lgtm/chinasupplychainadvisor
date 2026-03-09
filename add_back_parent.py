<!-- Back to Parent button -->
<div style="text-align: center; margin: 40px 0;">
  <button id="back-btn" style="
    padding: 12px 24px;
    background-color: #0b1f3a;
    color: white;
    border: none;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
  ">
    ← Back to Parent
  </button>
</div>

<script>
  const btn = document.getElementById('back-btn');
  btn.onmouseover = () => btn.style.backgroundColor = '#12325a';
  btn.onmouseout = () => btn.style.backgroundColor = '#0b1f3a';

  btn.onclick = function() {
    let path = window.location.pathname;
    if(path.endsWith('/')) path = path.slice(0, -1);
    const parent = path.substring(0, path.lastIndexOf('/'));
    window.location.href = parent === '' ? '/index.html' : parent + '/';
  };
</script>
