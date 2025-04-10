import streamlit as st
import pandas as pd
import streamlit.components.v1 as components



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

components.html(html_code, height=300)