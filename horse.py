import streamlit as st
import base64

# 页面基础配置
st.set_page_config(page_title="祝女王生日快乐", layout="centered")

video_file = "1.mp4" 

def get_base64_video(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    video_base64 = get_base64_video(video_file)

    # 终极竖屏适配 CSS
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #000000;
        }}
        .main-container {{
            position: relative;
            width: 100vw;
            height: 177.78vw; /* 严格 9:16 比例 */
            max-height: 85vh;
            margin: auto;
            overflow: hidden;
            background-color: black;
            border: 2px solid #FFD700;
        }}
        video {{
            width: 100%;
            height: 100%;
            object-fit: cover; /* 强制填满竖屏 */
        }}
        .overlay-text {{
            position: absolute;
            width: 85%;
            left: 50%;
            transform: translateX(-50%);
            bottom: 15%; /* 位置调低，不挡马头 */
            text-align: center;
            z-index: 10;
            background: rgba(0, 0, 0, 0.4); /* 半透明黑底，增加高级感 */
            padding: 15px;
            border-radius: 15px;
            color: gold;
            text-shadow: 2px 2px 4px #000;
            opacity: 0;
            animation: fadeInMove 4s ease-out 3.5s forwards;
        }}
        @keyframes fadeInMove {{
            from {{ opacity: 0; transform: translate(-50%, 20px); }}
            to {{ opacity: 1; transform: translate(-50%, 0); }}
        }}
        </style>
        
        <div class="main-container">
            <video id="queenVideo" autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
            <div class="overlay-text">
                <h2 style="font-size: 22px; margin: 0; color: gold;">致我心中永远的女王</h2>
                <p style="font-size: 16px; color: white; margin: 5px;">贺夫人<b>六十花甲</b>，岁在庚马</p>
                <p style="font-size: 14px; color: #ddd; margin: 2px;">姓冠“王”者 · 命属“马”者</p>
                <h3 style="color: #FF4500; font-size: 20px; margin-top: 8px;">60岁生日快乐！</h3>
            </div>
        </div>
        <script>
            // 尝试通过脚本再次确保自动播放
            var v = document.getElementById('queenVideo');
            v.play();
        </script>
    """, unsafe_allow_html=True)

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔊 开启女王专属音效"):
            st.info("请点击视频右下角的小喇叭开启声音")
    with col2:
        if st.button("✨ 接收万众祝福"):
            st.balloons()
            st.snow()

except FileNotFoundError:
    st.error("请确保文件名是 1.mp4")