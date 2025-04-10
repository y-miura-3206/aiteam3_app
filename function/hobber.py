import streamlit as st

html_code="""
<!DOCTYPE html>
<html lang = "ja">
<head>
    <meta charset ="UTF-8">
    <meta name"viewport" content="width=device-width, initial-scale=1.0">
    <title>グローバルナビ</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<section class="container">
    <ul>
        <li><a href="">ホーム</a></li>
        <li><a href="">企業情報</a></li>
        <li><a href="">事業内容</a></li>
        <li><a href="">サステナビリティ</a></li>
        <li><a href="">採用情報</a></li>
    </ul>
</section>
</body>
</html>
"""

css_code="""
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

.container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: sans-serif;
    background: □#000;
}

ul {
    padding: 0;
    margin: 0;
    display flex;
    flex-wrap: wrap;
    text-align: center;
}

ul li {
    list-style: none;
}

ul li a {
    text-decoration: none;
    color: ■#fff;
    font-size: 22px;
    padding: 1rem 2rem;
    position: relative;
    transition: color 1s;
}

ul li a:hover {
    color: ■#ffdab1;
}

a:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: ■#fff;
    transform: scaleX(0);
    transition: all 1s;
    transform-origin: left;
}

ul li a:hover:before,
ul li a:hover:after {
    transform: scaleX(1);
}

a:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: ■#fff;
    transform: scaleX(0);
    transition: all 1s;
    transform-origin: right;
}
"""

# st.markdown(f"""
# <style>
# {css_code}
# </style>

# {html_code}
# """, unsafe_allow_html=True)

# st.html(html_code)